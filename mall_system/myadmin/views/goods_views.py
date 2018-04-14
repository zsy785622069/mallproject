from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from myadmin.models import Types,Goods
import os

# 1. 商品添加
class GoodsAdd(View):
    def get(self,request):
        type_data = Types.objects.extra(select={'has': 'concat(path,id)'}).order_by('has')
        return render(request,'myadmin/goods_list/goods_add.html', {'type_data': type_data})

    def post(self,request):
        try:
            goods_post = request.POST
            gadd = Goods()
            gadd.title = goods_post.get('goods_name')  # 商品标题
            gadd.price = goods_post.get('goods_price')  # 商品价格
            gadd.storage = goods_post.get('goods_storage')  # 商品库存
            gadd.status = goods_post.get('goods_status')  # 商品状态

            gadd.info = goods_post.get('goods_info')   # 商品详情
            gadd.typeid = Types.objects.get(id=goods_post.get('goods_type_id'))  # 分类级别

            # 导入图片文件
            from my_public_package.my_models import filesload
            gadd.pic = filesload(request, 'goods_images', './static/myadmin/goods_images/')  # 商品图片

            gadd.save()
            return HttpResponse('<script>alert("添加成功");location.href="/myadmin/goods_index"</script>')
        except:
            return HttpResponse('<script>alert("添加失败");location.href="/myadmin/goods_add"</script>')

# 2. 商品列表
def goods_index(request):
    goods_data = Goods.objects.all()

    from my_public_package.page_info import PageInfo
    base_url = request.path_info
    get_par = request.GET
    args = ''
    for k,v in get_par.items():
        if k != 'p':
            args += "&%s=%s"%(k,v)
    if len(goods_data) == 0:
        goods_data = {}
        page_info = {}
    else:
        count_data = goods_data.count()
        page_info = PageInfo(request.GET.get('p'), 5, count_data, base_url, args)
        goods_data = goods_data[page_info.start():page_info.end()]
    return render(request, 'myadmin/goods_list/goods_index.html', {'goods_data': goods_data, 'page_info': page_info})


# 3. 商品修改
class GoodsUpdate(View):
    def get(self, request,up_id):
        goods_data = Goods.objects.get(id=up_id)
        type_data = Types.objects.extra(select={'has': 'concat(path,id)'}).order_by('has')
        return render(request,'myadmin/goods_list/goods_update.html',{'goods_data': goods_data, 'type_data': type_data})

    def post(self, request):
        try:
            post_data = request.POST
            goods_data = Goods.objects.get(id=post_data.get('goods_data_id'))
            print(goods_data)
            goods_data.title = post_data.get('goods_name')  # 商品标题
            goods_data.price = post_data.get('goods_price')  # 商品价格
            goods_data.storage = post_data.get('goods_storage')  # 商品库存
            goods_data.status = post_data.get('goods_status')  # 商品状态

            goods_data.info = post_data.get('goods_info')  # 商品详情
            goods_data.typeid = Types.objects.get(id=post_data.get('goods_type_id'))  # 分类级别

            if request.FILES.get('goods_images',None):
                # 导入图片文件
                filename = '.' + goods_data.pic
                print(filename)
                if os.path.exists(filename):
                    os.remove(filename)
                from my_public_package.my_models import filesload
                goods_data.pic = filesload(request, 'goods_images', './static/myadmin/goods_images/')  # 商品图片
            goods_data.save()
            return HttpResponse('<script>alert("修改成功");location.href="/myadmin/goods_index"</script>')
        except:
            return HttpResponse('<script>alert("修改失败");location.href="/myadmin/goods_index"</script>')


def goods_del(request, del_id):
    try:
        gd = Goods.objects.get(id=del_id)
        gd.delete()
        filename = '.' + gd.pic
        print(filename)
        if os.path.exists(filename):
            os.remove(filename)
        return HttpResponse('<script>alert("删除成功");location.href="/myadmin/goods_index"</script>')
    except:
        return HttpResponse('<script>alert("删除失败");location.href="/myadmin/goods_index"</script>')



