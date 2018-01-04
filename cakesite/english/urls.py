from django.conf.urls import url, handler404, handler500
from english import views

urlpatterns = [
    url(r'^$', views.enList, name='enList'),
    url(r'(?P<enid>\d+)/detail/$', views.enDetail, name='detail'),
    url(r'^more_list/$', views.more_list, name='more_list'),
]
