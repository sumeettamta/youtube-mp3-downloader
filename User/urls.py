from django.conf.urls import patterns,url

from . import views

urlpatterns = patterns('',
   # url(r'^admin/', include(admin.site.urls)),
    #url(r'^accounts/login/$', 'User.views.login'),
    #url(r'^accounts/auth/$', 'User.views.auth_view'),
    #url(r'^accounts/logout/$', 'User.views.logout'),
    #url(r'^accounts/loggedin/$', 'User.views.loggedin'),
    #url(r'^login/', include('User.urls')),
    #url(r'^accounts/invalid/$', 'User.views.invalid_login')
    #url(r'^accounts/login',include('User.views.urls'))
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'User.views.login'),
    url(r'^signup/$', 'User.views.register'),
    # url(r'^sucess/$', 'User.views.sucess'),
    url(r'^auth/$', 'User.views.auth_view'),
    url(r'^logout/$', 'User.views.logout'),
    url(r'^loggedin/$', 'User.views.loggedin'),
    #url(r'^login/', include('User.urls')),
    url(r'^invalid/$', 'User.views.invalid_login')
)




