from django.conf.urls import include, url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^download_page', views.downloadpage, name='download_page'),
    url(r'^download', views.download, name='download'),
    url(r'^history', views.userhistory, name='user_history'),
    # url(r'^suggestion', views.Suggestion, name='suggestions'),
    url(r'^search_results', views.youtube_search, name='search_results'),
    url(r'^search', views.search, name='search'),
    url(r'^songs/$', views.SongList.as_view()),
    url(r'^songs/(?P<pk>[0-9]+)/$', views.SongDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)