from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Users
import time
import os
MYADMAIN_USER_V1 = os.path.abspath(__file__)

# 会员列表
def index(request):
    data_list = Users.objects.exclude(delete_data='0')
    # 条件筛选
    #   lookup_data=sex&search_form=男
    search_col = ('username', 'sex', 'status')
    get_req = request.GET.get('lookup_data', None)
    get_con = request.GET.get('search_form', None)

    if get_req == 'username':
        data_list = data_list.filter(username__contains=get_con)
    elif get_req == 'sex':
        if get_con == '男':
            k = '1'
        elif get_con == '女':
            k = '0'
        else:
            k = '3'
        data_list = data_list.filter(sex__contains=k)


    from . mymodule.page_info import PageInfo
    base_url = request.path_info
    # 1). 获取 get 提交的参数
    get_par = request.GET
    # 2). 将 除 p 之外的其他参数 拼接起来
    args = ''
    for k,v in get_par.items():
        if k != 'p':
            args += "&%s=%s"%(k,v)
    if len(data_list) == 0:
        user_list = {}
        page_info = {}
    else:
        count_data = data_list.count()
        page_info = PageInfo(request.GET.get('p'), 10, count_data, base_url, args)
        user_list = data_list[page_info.start():page_info.end()]

    return render(request, 'myadmin/index.html',{'user_list':user_list, 'page_info': page_info})


# 会员添加
def useradd(request):
    return render(request, 'myadmin/add.html')

# 会员添加进数据库
def user_insert(request):
    from  django.contrib.auth.hashers import make_password
    # list1 = ['username', 'password', 'phone', 'email', 'address', 'age', 'sex', 'status']
    res = request.POST
    # try:
    uname = res['username']
    user_a = Users()
    user_a.username = res['username']
    user_a.password = make_password(res['password'], None, 'pbkdf2_sha256')
    user_a.phone = res['phone']
    user_a.email = res['email']
    user_a.address = res['address']
    user_a.age = res['age']

    if res['sex'] in ('0', '1'):
        user_a.sex = res['sex']
    else:
        a = '\033[1;31mERROR: \033[1;34m文件:%s\033[1;31m 年龄字段 插入 error , 插入价值不是男或女\033[0m' % (MYADMAIN_USER_V1)

        print(a)
        raise AttributeError(a)
    if res['status'] in ('0', '1', '2'):
        user_a.status = res['status']
    else:
        b = '\033[1;31mERROR: \033[1;34m文件:%s\033[1;31m 状态字段 插入 error, 插入值不正确\033[0m' %(MYADMAIN_USER_V1)
        print(b)
        raise AttributeError(b)

    # user_a.status = res['status']
    if request.FILES.get('pic',None):
        user_a.pic = filesload(request, uname)
    user_a.save()
    return HttpResponse('<script>alert("添加成功");location.href="/myadmin/"</script>')
    # except AttributeError as arterror:
    #     return HttpResponse('<script>alert("添加失败, 图片上传错误, 请重新添加");location.href="/myadmin/useradd"</script>')
    # except BaseException as be:
    #     return HttpResponse('<script>alert("添加失败, 字段指定错误请重新制定");location.href="/myadmin/useradd"</script>')

# 数据删除
def user_data_delele(request,uid):
    data_del = Users.objects.exclude(delete_data='0').filter(id=uid)
    if len(data_del) != 0:
        data_del[0].delete_data = '0'
        data_del[0].save()
        return HttpResponse('<script>alert("删除成功");location.href="/myadmin/"</script>')
    return HttpResponse('<script>alert("删除失败");location.href="/myadmin/"</script>')










# 上传照片
def filesload(request, user_uname):
    # 接受上传的文件
    myfile = request.FILES.get('pic',None)
    filename = "./static/public/pics/" + user_uname + "+" + str(time.time()) + '.' + myfile.name.split('.').pop()
    # 打开文件,写入
    with open(filename, "wb+") as f:
        for chunk in myfile.chunks():
            f.write(chunk)
    filename2 = filename.split(".", maxsplit=1)[1]
    return filename2



