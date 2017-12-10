from django.conf.urls import url, handler404
from . import views

urlpatterns = [
    url(r'^$', views.category, name='category'),
    url(r'^s', views.moreCake, name='moreCake'),
    url(r'(?P<category_id>\d)/$', views.cakeList, name='cakeList'),
    url(r'(?P<cake_id>\d+)/detail/$', views.cakeDetail, name='detail'),
]