from django.conf.urls import url, handler404
from . import views

urlpatterns = [
    url(r'^getOpenId', views.getOpenId, name='getOpenId'),
    url(r'^postUserInfo', views.postUserInfo, name='postUserInfo'),
    url(r'^postError', views.postError, name='postError'),
    url(r'^postSearch', views.postSearch, name='postSearch'),
    url(r'^getQQOpenId', views.getQQOpenId, name='getQQOpenId'),

]