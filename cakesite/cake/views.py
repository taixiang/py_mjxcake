from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Category, Cake, Message
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.core import serializers


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

    return render(request, "cake/cake.html", {"categorys": categorys, "allcake": allcake, "has_next": has_next, "message": message})


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

    return render(request, "cake/cake.html", {"categorys": categorys, "allcake": allcake, "has_next": has_next, "cake_id": int(category_id), "message": message})


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