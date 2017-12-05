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
    allcake = paginator.page(1)

    return render(request, "cake/cake.html", {"categorys": categorys, "allcake": allcake})


def cakeList(request, category_id):
    categorys = Category.objects.all()
    allcake = Cake.objects.filter(category_id=category_id)
    return render(request, "cake/cake.html", {"categorys": categorys, "allcake": allcake, "cake_id": int(category_id)})


def cakeDetail(request, cake_id):
    cake_detail = Cake.objects.get(id=cake_id)
    categorys = Category.objects.all()
    return render(request, "cake/detail.html", {"categorys": categorys, "detail": cake_detail})

