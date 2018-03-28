from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Category, Cake, Message
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.core import serializers
from cake.serialize import CakeListSerializer, ResultPagination, DetailSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import detail_route
from collections import OrderedDict
from rest_framework import viewsets, generics, renderers


# Create your views here.

def category(request):
    categorys = Category.objects.all()
    message = Message.objects.first()
    allData = Cake.objects.all()
    paginator = Paginator(allData, 10)
    page = request.GET.get('page')

    try:
        allcake = paginator.page(page)
    except PageNotAnInteger:
        allcake = paginator.page(1)
    except EmptyPage:
        allcake = paginator.page(paginator.num_pages)

    if allcake.has_next():
        has_next = True
    else:
        has_next = False

    return render(request, "cake/cake.html",
                  {"categorys": categorys, "allcake": allcake, "has_next": has_next, "message": message})


def cakeList(request, category_id):
    categorys = Category.objects.all()
    message = Message.objects.first()
    allData = Cake.objects.filter(category_id=category_id)
    paginator = Paginator(allData, 10)
    page = request.GET.get('page')

    try:
        allcake = paginator.page(page)
    except PageNotAnInteger:
        allcake = paginator.page(1)
    except EmptyPage:
        allcake = paginator.page(paginator.num_pages)

    if allcake.has_next():
        has_next = True
    else:
        has_next = False

    return render(request, "cake/cake.html",
                  {"categorys": categorys, "allcake": allcake, "has_next": has_next, "cake_id": int(category_id),
                   "message": message})


def moreCake(request):
    allCake = Cake.objects.all()
    paginator = Paginator(allCake, 10)
    page = request.GET.get('page')
    try:
        customer = paginator.page(page)
    except PageNotAnInteger:
        customer = paginator.page(1)
    except EmptyPage:
        customer = paginator.page(paginator.num_pages)
    data = serializers.serialize("json", customer)
    if customer.has_next():
        data = "{ \"data\":" + data + ",\"page\":" + page + ",\"next\":\"1\" }"
    else:
        data = "{ \"data\":" + data + ",\"page\":" + page + ",\"next\":\"\" }"

    return JsonResponse(data, safe=False)


def cakeDetail(request, cake_id):
    cake_detail = Cake.objects.get(id=cake_id)
    categorys = Category.objects.all()
    message = Message.objects.first()

    return render(request, "cake/detail.html", {"categorys": categorys, "detail": cake_detail, "message": message})


def page_not_find(request):
    return render(request, "cake/404.html")


# 接口

class CakeListViewSet(viewsets.ModelViewSet):
    pagination_class = ResultPagination
    queryset = Cake.objects.all()
    serializer_class = CakeListSerializer

    def list(self, request, *args, **kwargs):
        try:
            queryset = self.filter_queryset(self.get_queryset())
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


class DetailViewSet(viewsets.ModelViewSet):
    queryset = Cake.objects.all()
    serializer_class = DetailSerializer

    def retrieve(self, request, *args, **kwargs):
        try:
            pkid = kwargs.get('pk')
            data = Cake.objects.get(id=pkid)
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
