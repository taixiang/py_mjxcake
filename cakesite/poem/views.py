from django.db.models import Q
from django.http import JsonResponse, HttpResponse
from rest_framework import viewsets
from poem.serialize import PoemListSerializer, ResultPagination, PoetryListSerializer, PoemAuthorSerializer, \
    PoetryAuthorSerializer
from .models import Poems, Poetry, PoemsAuthor, PoetryAuthor, UserInfo
from rest_framework.response import Response
from collections import OrderedDict
import requests
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt


# Create your views here.


# 词
class PoemListViewSet(viewsets.ModelViewSet):
    pagination_class = ResultPagination
    queryset = Poems.objects.all()
    serializer_class = PoemListSerializer

    def list(self, request, *args, **kwargs):
        name = request.GET.get('name')
        if name is not None:
            self.queryset = self.queryset.filter(
                Q(title__contains=name) | Q(author__contains=name) | Q(content__contains=name))
        try:
            queryset = self.filter_queryset(self.queryset)
            page = self.paginate_queryset(queryset)

            if page is not None:
                serializer = self.get_serializer(page, many=True)

                return Response(OrderedDict([
                    ('code', 200),
                    ('count', self.paginator.page.paginator.count),
                    ('next', self.paginator.get_next_link()),
                    ('previous', self.paginator.get_previous_link()),
                    ('results', serializer.data)
                ]))

            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        except:
            return Response(OrderedDict([
                ('code', 500),
                ('results', None)
            ]))


class PoemAuthorViewSet(viewsets.ModelViewSet):
    queryset = PoemsAuthor.objects.all()
    serializer_class = PoemAuthorSerializer

    def list(self, request, *args, **kwargs):
        author = request.GET.get('author')
        self.queryset = self.queryset.filter(id=author)
        try:
            queryset = self.filter_queryset(self.queryset)
            serializer = self.get_serializer(queryset, many=True)
            return Response(OrderedDict([
                ('code', 200),
                ('results', serializer.data[0])
            ]))
        except:
            return Response(OrderedDict([
                ('code', 500),
                ('results', None)
            ]))


# 诗
class PoetryListViewSet(viewsets.ModelViewSet):
    pagination_class = ResultPagination
    queryset = Poetry.objects.all()
    serializer_class = PoetryListSerializer

    def list(self, request, *args, **kwargs):
        name = request.GET.get('name')
        if name is not None:
            self.queryset = self.queryset.filter(
                Q(title__contains=name) | Q(author__contains=name) | Q(content__contains=name))
        try:
            queryset = self.filter_queryset(self.queryset)
            page = self.paginate_queryset(queryset)

            if page is not None:
                serializer = self.get_serializer(page, many=True)

                return Response(OrderedDict([
                    ('code', 200),
                    ('count', self.paginator.page.paginator.count),
                    ('next', self.paginator.get_next_link()),
                    ('previous', self.paginator.get_previous_link()),
                    ('results', serializer.data)
                ]))

            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        except:
            return Response(OrderedDict([
                ('code', 500),
                ('results', None)
            ]))


class PoetryAuthorViewSet(viewsets.ModelViewSet):
    queryset = PoetryAuthor.objects.all()
    serializer_class = PoetryAuthorSerializer

    def list(self, request, *args, **kwargs):
        author = request.GET.get('author')
        self.queryset = self.queryset.filter(id=author)
        try:
            queryset = self.filter_queryset(self.queryset)
            serializer = self.get_serializer(queryset, many=True)
            return Response(OrderedDict([
                ('code', 200),
                ('results', serializer.data[0])
            ]))
        except:
            return Response(OrderedDict([
                ('code', 500),
                ('results', None)
            ]))


# 获取openid
def getOpenId(request):
    jscode = request.GET.get('code')
    print(jscode)
    print(111111)
    resp = requests.get(
        "https://api.weixin.qq.com/sns/jscode2session?appid=wxaba8acb899e024e2&secret=88ccaf6b28f01eb1c5e99e60289393eb&js_code=" + str(
            jscode) + "&grant_type=authorization_code")
    print(resp.text)
    # data = serializers.serialize("json", resp.text)
    return HttpResponse(json.dumps(resp.text), content_type="application/json")


@csrf_exempt
def postUserInfo(request):
    if request.method == 'POST':
        # data = request.POST['data']
        # json.load(request.text)

        data = json.loads(request.body)
        print(data['openId'])
        user = UserInfo.objects.filter(openId=data['openId'])
        print(user)
        if not user:
            print("==========")
            userInfo = UserInfo(nickName=data['nickName'], avatarUrl=data['avatarUrl'], gender=data['gender'],
                                language=data['language'], city=data['city'], province=data['province'],
                                country=data['country'], openId=data['openId'])
            userInfo.save()

    return JsonResponse(None, safe=False)
