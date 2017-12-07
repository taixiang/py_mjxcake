from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Category, Cake
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.core import serializers


# Create your views here.

def category(request):
    categorys = Category.objects.all()
    allData = Cake.objects.all()
    paginator = Paginator(allData, 1)
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

    return render(request, "cake/cake.html", {"categorys": categorys, "allcake": allcake, "has_next": has_next})


def cakeList(request, category_id):
    categorys = Category.objects.all()
    allData = Cake.objects.filter(category_id=category_id)
    paginator = Paginator(allData, 1)
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

    return render(request, "cake/cake.html", {"categorys": categorys, "allcake": allcake, "has_next": has_next, "cake_id": int(category_id)})


def moreCake(request):
    allCake = Cake.objects.all()
    paginator = Paginator(allCake, 1)
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
    return render(request, "cake/detail.html", {"categorys": categorys, "detail": cake_detail})
