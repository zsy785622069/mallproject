from django.shortcuts import render
from home.views.home_views import gettypeall
from myadmin.models import Types,Goods


def list_index(request, type_id):
    list_data = Types.objects.filter(id=type_id)[0]  # 获取 制定id 的
    type_rank = list_data.path.count(',')  # 获取分类级别
    if type_rank == 2:
        type_twn_rank = list_data.goods_set.all()
    else:
        type_twn_rank = []
        type_int_1 = Types.objects.filter(pid=type_id)
        for i in type_int_1:
             for v in i.goods_set.all():
                 type_twn_rank.append(v)

    twn_rank = Types.objects.exclude(pid=0) # 获取所有二级分类

    content = {
        'type_list': gettypeall,  # 导航条头部数据
        'type_twn_rank': type_twn_rank, # 二级列表数据
        'list_data':list_data,  # 当前的一级类
        'twn_rank': twn_rank    # 获取所有二级分类
    }
    return render(request, 'home/list.html', content)

def list_index_all(request):
    type_twn_rank = Goods.objects.filter()
    twn_rank = Types.objects.exclude(pid=0)
    content = {
        'type_list': gettypeall,  # 导航条头部数据
        'type_twn_rank': type_twn_rank, # 二级列表数据
        # 'list_data': list_data,  # 当前的一级类
        'twn_rank': twn_rank    # 获取所有二级分类
    }
    return render(request, 'home/list.html', content)
