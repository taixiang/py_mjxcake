from django.shortcuts import render
from english.models import learn
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.core import serializers


# Create your views here.

def enList(request):
    enList = learn.objects.all()
    paginator = Paginator(enList, 10)
    page = request.GET.get('page')
    try:
        customer = paginator.page(page)
    except PageNotAnInteger:
        customer = paginator.page(1)
    except EmptyPage:
        customer = paginator.page(paginator.num_pages)

    if customer.has_next():
        has_next = True
    else:
        has_next = False

    return render(request, "english/english.html", {"enList": customer, "has_next": has_next})


def more_list(request):
    enList = learn.objects.all()
    paginator = Paginator(enList, 10)
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


def enDetail(request, enid):
    detail = learn.objects.get(id=enid)
    return render(request, "english/detail.html", {"detail": detail})
