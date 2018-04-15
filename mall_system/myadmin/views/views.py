from django.shortcuts import render
from django.http import HttpResponse
from myadmin.models import Users
import time
import os
MYADMAIN_USER_V1 = os.path.abspath(__file__)

def home(request):
    return render(request, 'myadmin/users/home.html')

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
        elif get_con == '':
            k = ''
        else:
            k = '3'
        data_list = data_list.filter(sex__contains=k)
    elif get_req == 'status':
        # 普通用户 = 1 , 管理员用户 = 2 , 禁用用户 = 0
        if get_con == '普通用户':
            k = 1
        elif get_con in ('管理员用户', '管理员'):
            k = 2
        elif get_con in ('禁用用户', '已禁用'):
            k = 0
        elif get_con == '':
            k = ''
        else:
            k = 3
        data_list = data_list.filter(status=k)

    from my_public_package.page_info import PageInfo
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

    return render(request, 'myadmin/users/index.html', {'user_list':user_list, 'page_info': page_info})


# 会员添加
def useradd(request):
    return render(request, 'myadmin/users/add.html')

# 会员添加进数据库
def user_insert(request):
    from  django.contrib.auth.hashers import make_password
    # list1 = ['username', 'password', 'phone', 'email', 'address', 'age', 'sex', 'status']
    res = request.POST
    try:
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
            raise AttributeError("年龄字段 插入 error , 插入价值不是男或女, %s"%a)
        if res['status'] in ('0', '1', '2'):
            user_a.status = res['status']
        else:
            b = '\033[1;31mERROR: \033[1;34m文件:%s\033[1;31m 状态字段 插入 error, 插入值不正确\033[0m' %(MYADMAIN_USER_V1)
            print(b)
            raise AttributeError("状态字段 插入 error, 插入值不正确, %s"%b)

        # user_a.status = res['status']
        if request.FILES.get('pic',None):
            user_a.pic = filesload(request, uname)
        user_a.save()
        return HttpResponse('<script>alert("添加成功");location.href="/myadmin/user_index"</script>')
    except AttributeError as arterror:
        return HttpResponse('<script>alert("添加失败, 图片上传错误, 请重新添加");location.href="/myadmin/useradd"</script>')
    except BaseException as be:
        return HttpResponse('<script>alert("添加失败, 字段指定错误请重新制定");location.href="/myadmin/useradd"</script>')

# 数据删除
def user_data_delele(request,uid):
    data_del = Users.objects.exclude(delete_data='0').filter(id=uid)
    if len(data_del) != 0:
        data_del[0].delete_data = '0'
        data_del[0].save()
        return HttpResponse('<script>alert("删除成功");location.href="/myadmin/user_index"</script>')
    return HttpResponse('<script>alert("删除失败");location.href="/myadmin/user_index"</script>')

# 4. 数据修改
def user_data_update(request,us_id):
    obj = Users.objects.exclude(delete_data=0).filter(id=us_id)
    if len(obj) == 0:  #  说明 数据不 为空
        return HttpResponse('<script>alert("您查找的数据不存在");location.href="/myadmin/user_index"</script>')
    # return HttpResponse('user_data_update%s'%(us_id))
    return render(request, 'myadmin/users/update.html', {'obj':obj[0]})


# 5. 添加爱进数据库
def user_update_sql(request):
    from django.contrib.auth.hashers import make_password
    res = request.POST
    try:
        uname = res['username']
        user_a = Users.objects.exclude(delete_data=0).filter(id=res['id'])[0]
        user_a.username = res['username']
        if res['password'] != '':
            user_a.password = make_password(res['password'], None, 'pbkdf2_sha256')
        user_a.phone = res['phone']
        user_a.email = res['email']
        user_a.address = res['address']
        user_a.age = res['age']

        if res['sex'] in ('0', '1'):
            user_a.sex = res['sex']
        else:
            a = '\033[1;31mERROR: \033[1;34m文件:%s\033[1;31m 年龄字段 修改 error , 修改价值不是男或女\033[0m' % (MYADMAIN_USER_V1)
            print(a)
            raise AttributeError("年龄字段 修改 error , 修改 价值不是男或女, %s"%a)
        if res['status'] in ('0', '1', '2'):
            user_a.status = res['status']
        else:
            b = '\033[1;31mERROR: \033[1;34m文件:%s\033[1;31m 状态字段 修改 error, 修改值不正确\033[0m' %(MYADMAIN_USER_V1)
            print(b)
            raise AttributeError("状态字段 修改 error, 修改值不正确, %s"%b)

        # user_a.status = res['status']
        if request.FILES.get('pic',None):
            fil = filesload(request, uname)
            user_a.pic = fil
            request.session['user_pic'] = fil
        user_a.save()
        request.session['user_name'] = res['username']
        return HttpResponse('<script>alert("修改成功");location.href="/myadmin/user_index"</script>')
    except AttributeError as arterror:
        return HttpResponse('<script>alert("修改失败, 图片上传错误, 请重新修改");location.href="/myadmin/user_data_update/%s"</script>'%res['id'])
    except BaseException as be:
        return HttpResponse('<script>alert("修改失败, 字段指定错误请重新修改");location.href="/myadmin/user_data_update/%s"</script>'%res['id'])

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



