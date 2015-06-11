from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^download_page', views.downloadpage, name='download_page'),
    url(r'^download', views.download, name='download'),
    url(r'^history', views.userhistory, name='user_history'),
    # url(r'^suggestion', views.Suggestion, name='suggestions'),
    url(r'^search_results', views.youtube_search, name='search_results'),
    url(r'^search', views.search, name='search')
]