from django.shortcuts import render
from myadmin.models import Types, Goods
# from django.db.models import Q

def gettypeall():
    all_data = Types.objects.exclude(pid=0)
    return all_data

def index(request):
    # 1. 首页头部侧边导航栏
    type_data = Types.objects.all()
    arr = []
    for i in type_data.filter(pid=0):  # 循环第一次
        i.stu = type_data.filter(pid=i.id)
        for v in i.stu:
            v.stu = Goods.objects.filter(typeid_id=v.id)
        arr.append(i)
    # 2. 手机展示, 数据
    goods_list = Goods.objects.all()[:9]
    # 3. 热销商品
    re_xiao_list_1 = Goods.objects.all()[:5]
    re_xiao_list_2 = Goods.objects.all()[5:10]



    ret_value = {
        'type_list': gettypeall,
        'arr': arr,
        'goods_list': goods_list,
        're_xiao_list_1': re_xiao_list_1,
        're_xiao_list_2': re_xiao_list_2
    }
    return render(request, 'home/index.html', ret_value, )




