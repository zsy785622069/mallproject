from django.shortcuts import HttpResponse, render
from django.views import View
from home.models import Order,OrderInfo
from myadmin.models import Users, Goods
from home.views.home_views import gettypeall

class OrederAdd(View):
    def get(self, request):
        goods_list = request.session.get('order_add')
        return render(request, 'home/orderadd.html',{'goods_list': goods_list})

    def post(self, request):
        # request.session['order_'] = request.POST.get('goods_id_list')
        # request.session['login_users']['users_goods_id'] = request.POST.get('goods_id_list')
        goods_list = request.POST.get('goods_id_list').split(',')
        order_goods_id = [] # 用户存储用户选出的商品
        for i in goods_list: # 将用户选择的商品添加进订单列表
            order_goods_id.append(request.session.get('cart').get(i))
        request.session['order_add'] = order_goods_id
        return HttpResponse('orderadd')


def ordercreate(request):
    totail = 0  # 商品总价
    totail_num = 0
    for i in request.session['order_add']:
        totail += i['num']*i['price']
        totail_num += i['num']

    data = request.POST
    print(data)
    if data.get('consignee') and data.get('address') and data.get('phone') and data.get('code'):
        try:
            # 1. 添加订单数据信息
            oi = Order() # 添加订单数据
            oi.total_price = totail
            oi.total_number = totail_num
            oi.addcode = data.get('code') # 收获邮箱
            oi.addname = data.get('consignee') # 收获人
            oi.addphone = data.get('consignee') # 收获手机号
            oi.address = data.get('address') # 收获地址
            oi.uid = Users.objects.get(id=request.session['login_users']['user_id']) # 订单用户
            oi.status = 1 # 订单状态
            oi.save() # 保存数据

            # 2, 添加订单详情
            # print(request.session['order_add'])
            for i in request.session['order_add']:
                order_info_add = OrderInfo()
                order_info_add.num = i.get('num') # 商品数量
                order_info_add.price = i.get('price') # 商品单价
                order_info_add.orderid = oi
                order_info_add.gid = Goods.objects.get(id=i.get('id'))
                order_info_add.save()
                del request.session['cart'][str(i.get('id'))]
            if request.session.get('order_add'):
                del request.session['order_add']

            return HttpResponse('<script>alert("下单成功, 请支付");location.href="/buy/%s"</script>'%oi.id)
        except:
            return HttpResponse('<script>alert("订单信息错误, 请重新添加");location.href="/orderadd/"</script>')

    return HttpResponse('<script>alert("没有填写收获信息,请重新填写");location.href="/orderadd/"</script>')


def buy(request, oid): # oid 订单 id
    order = Order.objects.filter(id=oid)
    if len(order) == 1:
        if order[0].status == 1:
            print(order.query.__str__())
            return render(request, 'home/buy.html', {'order': order[0]})
    return HttpResponse('<script>alert("订单状态无需支付");location.href="/myorder/"</script>')


def pay(request, oid):
    order_pay = Order.objects.filter(status=1).filter(id=oid)
    print(order_pay.query.__str__())
    if len(order_pay) != 0:
        order_pay = order_pay[0]
        order_pay.status = 2
        order_pay.save()
    else:
        return HttpResponse('<script>alert("订单那状态无法, 再次支付");location.href="/myorder/"</script>')
    return HttpResponse('<script>alert("付款成功");location.href="/myorder/"</script>')

def myorder(request):
    user_order_data = Order.objects.filter(uid=request.session['login_users']['user_id']) # 获取用户的订单

    # info = user_order_data.orderinfo_set.all()
    # print(user_order_data)
    # print(info)

    content = {
        'user_order_data': user_order_data,
        'type_list': gettypeall
    }
    return render(request, 'home/myorder.html', content)
