from django.shortcuts import render, redirect,reverse
from django.http import HttpResponse
from myadmin.models import Types
from django.views import View

# 查看分类
def type_index(request):
    from myadmin.mymodule.page_info import PageInfo
    # type_data_all = Types.objects.all()
    type_data_all = Types.objects.extra(select= {'has': 'concat(path,id)'}).order_by('has')

    # 网页分页分页
    get_par = request.GET
    args = ''
    for k,v in get_par.items():
        if k != 'p':
            args += "&%s=%s"%(k,v)
    base_url = request.path_info
    page_info = PageInfo(request.GET.get('p'), 10, type_data_all.count(), base_url, args)
    return render(request, "myadmin/types_list/index.html", {'type_data_all': type_data_all,'page_info':page_info})


# CBV 添加分类
class TypeAdd(View):
    def get(self,request):
        # type_data = Types.objects.all()
        type_data = Types.objects.extra(select={'has': 'concat(path,id)'}).order_by('has')
        return render(request, "myadmin/types_list/type_add.html", {'type_data': type_data})

    def post(self,request):
        try:
            get_pid = request.POST.get('pid')
            tmq_add = Types()
            tmq_add.name = request.POST.get('type_name')
            tmq_add.pid = get_pid
            print('get_pid: ',get_pid)
            if get_pid == '0':
                res = '%s,'%get_pid
            else:
                tem = Types.objects.get(id=get_pid)
                res = '%s%s,'%(tem.path,get_pid)
                print('res: ',res)
            tmq_add.path = res
            tmq_add.save()
            # return render(request, "myadmin/types_list/index.html")
            return redirect(reverse('myadmin_type_index'))
        except:
            return render(request, "myadmin/types_list/index.html")

# 删除分类
def type_del(request, del_id):
    del_data = Types.objects.get(id=del_id)
    print(del_data)
    return HttpResponse('<script>alert("删除成功");location.href="/myadmin/type_index"</script>')
    # return HttpResponse('<script>alert("删除失败");location.href="/myadmin/useradd"</script>')

# def type_add(request):
#     if request.method == 'POST':
#         get_pid = request.POST.get('pid')
#         tmq_add = Types()
#         tmq_add.name = request.POST.get('type_name')
#         tmq_add.pid = get_pid
#         print(get_pid)
#         if get_pid == '0':
#             res = '{},'.format(get_pid)
#         else:
#             tem = Types.objects.filter(id=get_pid)[0].name
#             print('tem: ',tem)
#             res = '{},{},'.format(tem,get_pid)
#             print('res: ',res)
#         tmq_add.path = res
#         tmq_add.save()
#         return render(request, "myadmin/types_list/index.html")
#
#     type_data = Types.objects.all()
#     return render(request, "myadmin/types_list/type_add.html", {'type_data': type_data})


