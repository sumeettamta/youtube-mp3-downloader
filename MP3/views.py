from django.shortcuts import render
from downloads.models import Songs, UserHistory
from User.models import User
from django.http import HttpResponseRedirect, Http404
import urllib
import json
import os
import youtube_dl
import pdb

opt = {
    'format': 'bestaudio/best',
    'extractaudio': True,
    'audioformat': "mp3",
    'outtmpl': '%(id)s',
    'noplaylist': True
}


def home(request):
    if 'm_id' in request.session:
        user = User.objects.get(id=request.session['m_id'])
        songs = Songs.objects.all().order_by('-id')[:9]
        lp = "https://www.youtube.com/watch?v="
        if 'dl' in request.GET and request.GET['dl']:
            dl = request.GET['dl']
            lb = dl.split('=')
            if len(lb) == 1:
                dl = lp + dl
            ydl = youtube_dl.YoutubeDL(opt)
            r = None
            url = dl
            cwd = os.getcwd()
            try:
                yl = Songs.objects.get(youtube_link=dl)
                yl.download_count += 1
                yl.save()
                return render(request, 'home.html', {'songs': songs})
            except Songs.DoesNotExist:
                try:
                    os.chdir('/home/kuliza219/django/ENV/MP3/static/Downloaded Songs')
                    with ydl:
                        r = ydl.extract_info(url, download=True)
                    title = r['title']
                    json_data = json.loads(urllib.urlopen("https://www.googleapis.com/youtube/v3/videos?id=%s&key=AIzaSyAauLfeOKokwDqETGYcW7ppEP81JWVq15I&part=snippet,statistics" % r['id']).read())
                    thumbnail = json_data['items'][0]['snippet']['thumbnails']['high']['url']
                    # statistics = json_data['items'][0]['statistics']
                    os.rename(r['id'], "%s.mp3" % title)
                    d_link = 'Downloaded Songs' + '/' + title + ".mp3"
                    p = Songs(youtube_link=dl, local_link=d_link, title=r['title'], uploader=r['uploader'], \
                              view_count=r['view_count'], like_count=r['like_count'], unlike_count=r['dislike_count'], \
                              download_count=1, thumbnail=thumbnail)
                    p.save()
                    user, created = User.objects.get_or_create(id=request.session['m_id'])
                    if created:
                        us = UserHistory(user=user)
                        us.save()
                        us.song.add(p)
                    else:
                        us = UserHistory.objects.get(user=user)
                        us.song.add(p)
                    os.chdir(cwd)
                    return render(request, 'home.html', {'songs': songs, 'name': user.first_name})
                except Exception:
                    return render(request, 'home.html', {'songs': songs, 'name': user.first_name, 'error': True})
        else:
            return render(request, 'home.html', {'songs': songs, 'name': user.first_name})
    else:
        return HttpResponseRedirect('/accounts/login')


def temp(request):
    total_data = Songs.objects.all().count()
    if 'count' in request.GET and request.GET['count']:
        c = request.GET['count']
        t = int(c)
        if t-3 < total_data:
            temps = Songs.objects.all().order_by('-id')[:t]
            songs = temps[t-3:t]
            return render(request, 'temp.html', {'songs': songs})
        else:
            raise Http404
    else:
        raise Http404


def loginhome(request):
    if 'm_id' in request.session:
        return HttpResponseRedirect('/home')
    else:
        songs = Songs.objects.all().order_by('-id')[:9]
        context = {'songs': songs}
        template = 'loginhome.html'
        return render(request, template, context)
