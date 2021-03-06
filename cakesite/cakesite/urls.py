"""cakesite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include, handler404
from django.contrib import admin
from cake import views as cake_view
from poem import views as poem_view
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
import os

router = routers.DefaultRouter()
router.register(r'cakelist', cake_view.CakeListViewSet, base_name='cakeist')
router.register(r'detail', cake_view.DetailViewSet, base_name='detail')
router.register(r'poem', poem_view.PoemListViewSet, base_name='poem')
router.register(r'poem_author', poem_view.PoemAuthorViewSet, base_name='poem_author')
router.register(r'poetry', poem_view.PoetryListViewSet, base_name='poetry')
router.register(r'poetry_author', poem_view.PoetryAuthorViewSet, base_name='poetry_author')
router.register(r'poemdetail', poem_view.PoemDetailViewSet, base_name='poemdetail')
router.register(r'poetrydetail', poem_view.PoetryDetailViewSet, base_name='poetrydetail')
router.register(r'recommed', poem_view.RecommendViewSet, base_name='recommed')
router.register(r'myerror', poem_view.MyErrorViewSet, base_name='myerror')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^cake/', include('cake.urls', namespace='cake', app_name='cake')),
    url(r'^$', cake_view.category),
    url(r'^english/', include('english.urls', namespace='english', app_name='english')),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^poem/', include('poem.urls', namespace='poem', app_name='poem'))

]

if settings.DEBUG:
    media_root = os.path.join(settings.BASE_DIR, 'upload/img')
    urlpatterns += static('/upload/img/', document_root=media_root)
handler404 = cake_view.page_not_find
