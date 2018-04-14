from django.shortcuts import render, redirect,reverse
from django.http import HttpResponse
from myadmin.models import Types
from django.views import View

# 1. 查看分类列表
def type_index(request):
    from my_public_package.page_info import PageInfo
    type_data_all = Types.objects.extra(select= {'has': 'concat(path,id)'}).order_by('has')

    # 网页分页分页
    get_par = request.GET
    args = ''
    for k,v in get_par.items():
        if k != 'p':
            args += "&%s=%s"%(k,v)
    if len(type_data_all) == 0:
        type_data_all = {}
        page_info = {}
    else:
        base_url = request.path_info
        page_info = PageInfo(request.GET.get('p'), 5, type_data_all.count(), base_url, args)
        type_data_all = type_data_all[page_info.start():page_info.end()]
    return render(request, "myadmin/types_list/index.html", {'type_data_all': type_data_all,'page_info':page_info})


# 2. 添加分类
class TypeAdd(View):
    def get(self,request):
        type_data = Types.objects.extra(select={'has': 'concat(path,id)'}).order_by('has')
        return render(request, "myadmin/types_list/type_add.html", {'type_data': type_data})

    def post(self,request):
        try:
            get_pid = request.POST.get('pid')
            tmq_add = Types()
            tmq_add.name = request.POST.get('type_name')
            tmq_add.pid = get_pid
            if get_pid == '0':
                res = '%s,'%get_pid
            else:
                tem = Types.objects.get(id=get_pid)
                res = '%s%s,'%(tem.path,get_pid)
            tmq_add.path = res
            tmq_add.save()
            # return render(request, "myadmin/types_list/index.html")
            return redirect(reverse('myadmin_type_index'))
        except:
            return render(request, "myadmin/types_list/index.html")


# 3. 删除分类
def type_del(request, del_id):
    del_data = Types.objects.filter(pid=del_id) # 检测 要删除的分类下面有没有子类
    if len(del_data) != 0:
        return HttpResponse('<script>alert("删除失败, 您要删除分类有子类, 无法删除");location.href="/myadmin/type_index"</script>')

    dd = Types.objects.filter(id=del_id)
    if len(dd) == 0:
        return HttpResponse('<script>alert("删除失败, 没有这个字段");location.href="/myadmin/type_index"</script>')
    dd[0].delete()
    return HttpResponse('<script>alert("删除成功");location.href="/myadmin/type_index"</script>')



# 4. 分类修改
class TypeUpdate(View):
    def get(self,request,up_id):
        all_data = Types.objects.extra(select={'has': 'concat(path,id)'}).order_by('has')
        up = Types.objects.get(id=up_id)
        return render(request,'myadmin/types_list/updata_edit.html', {'all_data':all_data,'up' : up })

    def post(self, request):
        try:
            upid = request.POST.get('tid')
            print(request.POST)
            upname = request.POST.get('type_name')
            if upname == '':
                return HttpResponse('<script>alert("修改失败, 请重新修改");location.href="/myadmin/type_index"</script>')
            print(upid, type(upid))
            up_data = Types.objects.get(id=upid)
            up_data.name = upname
            up_data.save()
            return HttpResponse('<script>alert("修改成功");location.href="/myadmin/type_index"</script>')
        except:
            return HttpResponse('<script>alert("修改失败, 请重新修改");location.href="/myadmin/type_index"</script>')




