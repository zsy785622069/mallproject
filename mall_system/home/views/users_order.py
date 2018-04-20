from django.shortcuts import HttpResponse


def orderadd(request):
    return HttpResponse('orderadd')


def ordercreate(request):
    return HttpResponse('ordercreate')


def buy(request):
    return HttpResponse('buy')


def myorder(request):
    return HttpResponse('myorder')


def users_index(request):
    return HttpResponse('users_index')