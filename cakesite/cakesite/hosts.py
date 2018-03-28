from django_hosts import patterns, host  # 导入django-host
from django.conf import settings  # 导入settings
from english import views
from cake import views

host_patterns = patterns(
    '',
    host(r'www', 'cake.urls', name='www'),  # 子域名，类似weather.test.com中的weather
    # host(r'english', 'english.urls', name='english'),  # 子域名，类似translate.test.com 中的translate
)
