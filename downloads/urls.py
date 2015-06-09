from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^download_page', views.downloadpage, name='download_page'),
    url(r'^download', views.download, name='download'),
    url(r'^history', views.userhistory, name='user-history'),
    # url(r'^suggestion', views.Suggestion, name='suggestions'),
    url(r'^datetime', views.current_datetime, name='datetime'),
]