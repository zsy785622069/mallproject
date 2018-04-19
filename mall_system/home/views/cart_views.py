from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse,JsonResponse
from home.views.home_views import gettypeall
from myadmin.models import Goods
from django.views import View



class CartIndex(View):
    """
        负责处理购物车的数据请求
    """
    def get(self,request):
        cart = request.session.get('cart')
        content = {
            'cart': cart,
            'type_list': gettypeall
        }
        return render(request, 'home/cart.html', content)

    def post(self,request):
        cpg_id = request.POST.get('goods_id')  # 获取 用户提交的 商品的 id
        cpg_num = int(request.POST.get('goods_number'))  #  获取 用户提交的 商品的 价格
        sess_data = request.session.get('cart',{})

        if cpg_id in sess_data:
            # 如果商品存在的话就添加爱一个值
            sess_data[cpg_id]['num'] += cpg_num
        else:
            # 当商品不存在时 添加数据
            goods = Goods.objects.filter(id=cpg_id)[0] # 从数据库值中获取所系要的商品的信息
            # 组购物车需要的数据
            arr = {
                'id': goods.id,
                'title': goods.title,  # 商品 标题
                'pic': goods.pic,      # 商品 图片
                'price': float(goods.price),  # 商品 价格
                'num': cpg_num   # 商品 数量
            }
            sess_data[cpg_id] = arr  # 将 新添加的数据 添加进购物车
        request.session['cart'] = sess_data

        return redirect(reverse('home_cart'))

def cart_clear(request):
    """
        负责清空购物车
    """
    request.session['cart'] = {}
    return HttpResponse('cart_clear')

def cart_update(request):
    """ 负责修改购物车数量 """
    gid = request.GET.get('gid')
    num = request.GET.get('num')
    cart = request.session.get('cart', {})
    cart[gid]['num'] = int(num)
    request.session['cart'] = cart
    return HttpResponse("111")































# class CartIndex(View):
#     def get(self,request):
#         goods_data = []
#         for k in request.session.get('goods_detail',{}).keys():
#             app = Goods.objects.filter(id=k).values()[0]
#             gn = int(request.session.get("goods_detail").get(k).get("goods_number"))
#             app.update({'goods_number': gn})
#             print('title', app['title'] , type(app['title']))
#             print('price', app['price'] , type(app['price']))
#             goods_data.append(app)
#             print('goods_number', app['goods_number'] , type(app['goods_number']))
#
#         context = {'type_list': gettypeall,'goods_data':goods_data,}
#         return render(request, 'home/cart_bak.html', context)
#
#     def post(self,request):
#         cart_post = request.POST
#         sess_goods = request.session.get('goods_detail')
#         cpg_id = cart_post.get('goods_id')
#         cpg_num = cart_post.get('goods_number')
#
#         if sess_goods:
#             if cpg_id in sess_goods:
#                 a1 = sess_goods.get(cpg_id)
#                 a1_num = int(a1['goods_number'])
#                 a1['goods_number'] = a1_num + int(cpg_num)
#
#             elif cpg_id:
#                 old = request.session['goods_detail']
#                 old.update({cpg_id: {'goods_id': cpg_id,'goods_number': cpg_num}})
#                 request.session['goods_detail'] = old
#         elif cpg_id:
#             request.session['goods_detail'] = {cpg_id: {'goods_id': cpg_id, 'goods_number': int(cpg_num)}}
#         return redirect(reverse('home_cart'))


# def cart_index_add(request):
#     goods_data = []
#     for k in request.session.get('goods_detail',{}).keys():
#         app = Goods.objects.filter(id=k).values()[0]
#         gn = request.session.get("goods_detail").get(k).get("goods_number")
#         app.update({'goods_number': gn})
#         goods_data.append(app)
#
#     context = {'type_list': gettypeall,'goods_data':goods_data,}
#     return render(request, 'home/cart_bak.html', context)
#
# def cart_index(request):
#     cart_post = request.POST
#     sess_goods = request.session.get('goods_detail')
#     cpg_id = cart_post.get('goods_id')
#     cpg_num = cart_post.get('goods_number')
#
#     if sess_goods:
#         if cpg_id in sess_goods:
#             a1 = sess_goods.get(cpg_id)
#             a1_num = int(a1['goods_number'])
#             a1['goods_number'] = str(a1_num + int(cpg_num))
#
#         elif cpg_id:
#             old = request.session['goods_detail']
#             old.update({cpg_id: {'goods_id': cpg_id,'goods_number': cpg_num}})
#             request.session['goods_detail'] = old
#     elif cpg_id:
#         request.session['goods_detail'] = {cpg_id: {'goods_id': cpg_id, 'goods_number': cpg_num}}
#     # return HttpResponse('<script>alert("1111");location.href="/cart_get"</script>')
#     return redirect(reverse('home_cart_get'))






