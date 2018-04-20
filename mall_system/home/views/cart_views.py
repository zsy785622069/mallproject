from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse,JsonResponse
from home.views.home_views import gettypeall
from myadmin.models import Goods
from django.views import View


class CartIndex(View):
    """ 负责处理购物车的数据请求 """
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


# 修改用户的商品数量
def cart_update(request):
    """ 负责修改购物车数量 """
    gid = request.GET.get('gid')
    num = request.GET.get('num')
    cart = request.session.get('cart', {})
    cart[gid]['num'] = int(num)
    request.session['cart'] = cart
    return HttpResponse("update_ok")


# 删除用户商品
def cart_del(request):
    gid = request.GET.get('del_id')
    cart = request.session.get('cart', {})
    del cart[gid]
    return HttpResponse("del_ok")













