from django.conf.urls import include, url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
	url(r'^cart/$', views.CartList.as_view()),
    url(r'^cart/(?P<pk>[0-9]+)/$', views.CartDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)