from django.shortcuts import render
from downloads.models import Songs
from django.http import HttpResponseRedirect
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
    ids = []
    thumbnails = []
    titles = []
    songs = Songs.objects.all().order_by('-id')[:6]
    s = len(songs)
    # pdb.set_trace()
    songs = songs[s-6:s]
    print s
    for song in songs:
        id = song.youtube_link.split('=')
        title = song.title
        ids.append(id[1])
        titles.append(title)

    for id in ids:
        json_data = json.loads(urllib.urlopen("https://www.googleapis.com/youtube/v3/videos?id=%s&key=AIzaSyAauLfeOKokwDqETGYcW7ppEP81JWVq15I&part=snippet,statistics" % id).read())
        # pdb.set_trace()
        statistics = json_data['items'][0]['statistics']
        thumbnail = json_data['items'][0]['snippet']['thumbnails']['high']['url']
        thumbnails.append(thumbnail)

    zipped = zip(thumbnails, titles)

    # return render(request, 'home.html', {'zipped': zipped})

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
            # d_link = yl.local_link
            return render(request, 'home.html', {'zipped': zipped})
        except Songs.DoesNotExist:
            try:
                os.chdir('/home/kuliza219/django/ENV/MP3/static/Downloaded Songs')
                with ydl:
                    r = ydl.extract_info(url, download = True)
                title = r['title']

                os.rename(r['id'], "%s.mp3" % title)
                d_link = 'Downloaded Songs' + '/' + title + ".mp3"
                p = Songs(youtube_link=dl, local_link=d_link, title=r['title'], uploader=r['uploader'], \
                          view_count=r['view_count'], like_count=r['like_count'], unlike_count=r['dislike_count'], \
                          download_count=1)
                p.save()
                os.chdir(cwd)
                # return render(request, 'home.html', {'zipped': zipped})
                return HttpResponseRedirect('home/')
            except Exception:
                return render(request, 'home.html', {'zipped': zipped})
    else:
        return render(request, 'home.html', {'zipped': zipped})

