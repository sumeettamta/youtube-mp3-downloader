import os
import httplib2
from oauth2client import xsrfutil
from oauth2client.client import flow_from_clientsecrets
from oauth2client.django_orm import Storage
from googleapiclient.discovery import build
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.conf import settings
import pdb
from .models import CredentialsModel, FlowModel
 
CLIENT_SECRETS = os.path.join(settings.BASE_DIR, 'MP3', 'client_secrets.json')
 
YOUTUBE_READONLY_SCOPE = "https://www.googleapis.com/auth/youtube.readonly"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"


@login_required
def index(request):
    REDIRECT_URI = 'http://localhost:8000/oauth2/oauth2callback'
    # REDIRECT_URI = "https://%s%s" % (
    #     get_current_site(request).domain, reverse("oauth2:return"))
    FLOW = flow_from_clientsecrets(
        CLIENT_SECRETS,
        scope='https://www.googleapis.com/auth/youtube.readonly',
        redirect_uri=REDIRECT_URI
    )
    user = request.user
    storage = Storage(CredentialsModel, 'id', user, 'credential')
    credential = storage.get()
    if credential is None or credential.invalid is True:
        FLOW.params['state'] = xsrfutil.generate_token(
            settings.SECRET_KEY, user)
        authorize_url = FLOW.step1_get_authorize_url()
        f = FlowModel(id=user, flow=FLOW)
        f.save()
        return HttpResponseRedirect(authorize_url)
    else:
        http = httplib2.Http()
        http = credential.authorize(http)
        youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, http=http)
        channels_response = youtube.channels().list(
            mine=True,
            part="contentDetails"
        ).execute()

        for channel in channels_response["items"]:
            wh_list_id = channel["contentDetails"]["relatedPlaylists"]["watchHistory"]

            playlistitems_list_response = youtube.playlistItems().list(
                playlistId=wh_list_id,
                part="snippet",
                maxResults=50,
            ).execute()

            video_id = []
            for playlist_item in playlistitems_list_response["items"]:
                video_id.append(playlist_item["snippet"]["resourceId"]["videoId"])
            video_ids = ','.join(video_id)

            video_response = youtube.videos().list(
                id=video_ids,
                part='snippet',
            ).execute()

            titles = []
            video_id = []
            for vr in video_response['items']:
                if vr['snippet']['categoryId'] == "10":
                    titles.append(vr["snippet"]["title"])
                    video_id.append("https://www.youtube.com/watch?v=" + vr['id'])

            details = zip(titles, video_id)
        # pdb.set_trace()
        return details
        # return render(request, 'welcome.html', {'details': details})


@login_required
def auth_return(request):
    user = request.user
    if not xsrfutil.validate_token(
            settings.SECRET_KEY, str(request.GET['state']), user):
        return HttpResponseBadRequest()
    FLOW = FlowModel.objects.get(id=user).flow
    credential = FLOW.step2_exchange(request.GET)
    storage = Storage(CredentialsModel, 'id', user, 'credential')
    storage.put(credential)
    return HttpResponseRedirect("/oauth2")

@login_required
def logout(request):
    u = request.user
    f = FlowModel.objects.get(id=u.id)
    f.delete()
    c = CredentialsModel.objects.get(id=u.id)
    c.delete()
    storage = Storage(CredentialsModel, 'id', u, 'credential')
    storage.delete()
    return HttpResponseRedirect("http://accounts.google.com/logout")