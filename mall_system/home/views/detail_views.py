from django.shortcuts import render
from myadmin.models import Goods
from home.views.home_views import gettypeall


def detail_index(request, goods_id):
    goods_detail = Goods.objects.filter(id=goods_id)[0]
    return render(request, 'home/detail.html', {'type_list': gettypeall,'goods_detail': goods_detail})






