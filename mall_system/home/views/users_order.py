from django.shortcuts import HttpResponse, render
from django.views import View



class OrederAdd(View):
    def get(self, request):
        print(request.session.get('order_add'))
        goods_list = request.session.get('order_add')
        # import json
        # return HttpResponse(json.dumps(goods_list))

        # 用户名:
        request.session.get('login_users')

        return render(request, 'home/orderadd.html',{'goods_list': goods_list})

    def post(self, request):
        print(request.POST)
        goods_list = request.POST.get('goods_id_list').split(',')
        order_goods_id = [] # 用户存储用户选出的商品
        for i in goods_list: # 将用户选择的商品添加进订单列表
            order_goods_id.append(request.session.get('cart').get(i))
        request.session['order_add'] = order_goods_id
        print("order_goods_id", order_goods_id)
        return HttpResponse('orderadd')


def ordercreate(request):
    return HttpResponse('ordercreate')


def buy(request):
    return HttpResponse('buy')


def myorder(request):
    return HttpResponse('myorder')


def users_index(request):
    return HttpResponse('users_index')