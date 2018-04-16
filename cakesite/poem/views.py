from django.db.models import Q
from django.http import JsonResponse, HttpResponse
from rest_framework import viewsets
from poem.serialize import PoemListSerializer, ResultPagination, PoetryListSerializer, PoemAuthorSerializer, \
    PoemDetailSerializer, PoetryAuthorSerializer, PoetryDetailSerializer, RecommendSerializer,MyErrorSerializer
from .models import Poems, Poetry, PoemsAuthor, PoetryAuthor, UserInfo, ErrorInfo, SearchInfo, Recommend
from rest_framework.response import Response
from collections import OrderedDict
import requests
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt
import time


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


class PoemDetailViewSet(viewsets.ModelViewSet):
    queryset = Poems.objects.all()
    serializer_class = PoemDetailSerializer

    def list(self, request, *args, **kwargs):
        return Response(OrderedDict([
            ('code', 500),
            ('results', None)
        ]))

    def retrieve(self, request, *args, **kwargs):
        try:
            pkid = kwargs.get('pk')
            print(pkid)
            if pkid is None:
                return Response(OrderedDict([
                    ('code', 500),
                    ('results', None)
                ]))

            data = Poems.objects.get(id=pkid)
            serializer = self.get_serializer(data)
            return Response(OrderedDict([
                ('code', 200),
                ('results', serializer.data)
            ]))
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


class PoetryDetailViewSet(viewsets.ModelViewSet):
    queryset = Poetry.objects.all()
    serializer_class = PoetryDetailSerializer

    def list(self, request, *args, **kwargs):
        return Response(OrderedDict([
            ('code', 500),
            ('results', None)
        ]))

    def retrieve(self, request, *args, **kwargs):
        try:
            pkid = kwargs.get('pk')
            data = Poetry.objects.get(id=pkid)
            serializer = self.get_serializer(data)
            return Response(OrderedDict([
                ('code', 200),
                ('results', serializer.data)
            ]))
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


# 用户信息保存
@csrf_exempt
def postUserInfo(request):
    if request.method == 'POST':

        data = json.loads(request.body.decode('utf-8'))
        print(data['openId'])
        user = UserInfo.objects.filter(openId=data['openId'])
        print(user)
        if not user:
            print("==========")
            userInfo = UserInfo(**data)
            userInfo.save()
        elif 'nickName' in data.keys():
            print("------")
            user.update(**data)


    return JsonResponse(None, safe=False)


# 纠错信息
@csrf_exempt
def postError(request):
    print("===================")
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        ErrorInfo(**data).save()
        result = "{ \"code\":" + "200" + ",\"result\":" + "\"提交成功\"}"

    return JsonResponse(result, safe=False)


# 搜索内容
@csrf_exempt
def postSearch(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        SearchInfo(**data).save()

    return JsonResponse(None, safe=False)


# 推荐内容
class RecommendViewSet(viewsets.ModelViewSet):
    queryset = Recommend.objects.all()
    serializer_class = RecommendSerializer

    def list(self, request, *args, **kwargs):
        try:
            localtime = time.localtime()
            weekDay = time.strftime("%w", localtime)
            self.queryset = self.queryset.filter(week=weekDay)[:1]  # 取最新的一条
            serializer = self.get_serializer(self.queryset, many=True)
            return Response(OrderedDict([
                ('code', 200),
                ('results', serializer.data)
            ]))
        except:
            return Response(OrderedDict([
                ('code', 500),
                ('results', None)
            ]))


# 我的纠错
class MyErrorViewSet(viewsets.ModelViewSet):
    pagination_class = ResultPagination
    queryset = ErrorInfo.objects.all()
    serializer_class = MyErrorSerializer

    def list(self, request, *args, **kwargs):
        openId = request.GET.get('openId')
        if openId is not None:
            print("==============")
            self.queryset = self.queryset.filter(openId=openId)
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
