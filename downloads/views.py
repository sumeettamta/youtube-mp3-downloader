from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from downloads.models import Songs
import datetime
import youtube_dl
import os

options = {
    'format': 'bestaudio/best',
    'extractaudio': True,
    'audioformat': "mp3",
    'outtmpl': '%(id)s',
    'noplaylist': True
}


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


def downloadpage(request):
    return render(request, 'download.html')


def download(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        ydl = youtube_dl.YoutubeDL(options)
        r = None
        url = q
        cwd = os.getcwd()
        try:
            yl = Songs.objects.get(youtube_link=q)
            yl.download_count += 1
            yl.save()
            d_link = yl.local_link
        except Songs.DoesNotExist:
            os.chdir('/home/kuliza219/django/ENV/MP3/static/Downloaded Songs')
            with ydl:
                r = ydl.extract_info(url, download = True)
            title = r['title']

            os.rename(r['id'], "%s.mp3" % title)
            d_link = 'Downloaded Songs' + '/' + title + ".mp3"
            p = Songs(youtube_link=q, local_link=d_link, title=r['title'], uploader=r['uploader'], \
                      view_count=r['view_count'], like_count=r['like_count'], unlike_count=r['dislike_count'], \
                      download_count=1)
            p.save()
        print d_link
        os.chdir(cwd)
        return render(request, 'download_file.html', {'d_link': d_link, 'query': q})
    else:
        return render(request, 'download.html', {'error': True})

def userhistory(request):
    songs = Songs.objects.all()
    print songs
    return render(request, 'history.html', {'songs': songs})
