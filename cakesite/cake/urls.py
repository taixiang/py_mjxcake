from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.category, name='category'),
    url(r'(?P<category_id>\d)/$', views.cakeList, name='cakeList'),
    url(r'(?P<cake_id>\d+)/detail/$', views.cakeDetail, name='detail'),
]