from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from myadmin.models import Types,Goods

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












# # 上传照片 函数
# def filesload(request, image_dict_key, files_path):
#     '''
#     上传照片 函数
#     :param request:
#     :param image_dict_key:
#     :param files_path:
#     :return:
#     '''
#     from my_public_package.my_models import ramdom_num
#     # 接受上传的文件
#     myfile = request.FILES.get(image_dict_key, None)
#     # filename = "./static/myadmin/goods_images/" + ramdom_num(8) + str(time.time()) + '.' + myfile.name.split('.').pop()
#     filename = files_path + ramdom_num(8) + str(time.time()) + '.' + myfile.name.split('.').pop()
#     # 打开文件,写入
#     with open(filename, "wb+") as f:
#         for chunk in myfile.chunks():
#             f.write(chunk)
#     filename2 = filename.split(".", maxsplit=1)[1]
#     return filename2