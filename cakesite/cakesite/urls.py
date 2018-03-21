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
from cake import views
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
import os

router = routers.DefaultRouter()
router.register(r'cakelist', views.CakeListViewSet, base_name='cakeist')
router.register(r'detail', views.DetailViewSet, base_name='detail')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^cake/', include('cake.urls', namespace='cake', app_name='cake')),
    url(r'^$', views.category),
    url(r'^english/', include('english.urls', namespace='english', app_name='english')),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]

if settings.DEBUG:
    media_root = os.path.join(settings.BASE_DIR, 'upload/img')
    urlpatterns += static('/upload/img/', document_root=media_root)
handler404 = views.page_not_find
