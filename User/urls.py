from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url(r'^login/$', 'User.views.login'),
    url(r'^signup/$', 'User.views.register'),
    url(r'^auth/$', 'User.views.auth_view'),
    url(r'^logout/$', 'User.views.logout'),
)




