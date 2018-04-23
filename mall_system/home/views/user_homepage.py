from django.shortcuts import render, HttpResponse
from home.views.home_views import gettypeall
from myadmin.models import Users
from django.views import View
import os
MYADMAIN_USER_V1 = os.path.abspath(__file__)
from my_public_package.my_models import filesload


def user_homepage(request):
    res = request.session.get('login_users').get('user_id')
    user_data = Users.objects.get(id=res)  # 查找用户信息

    user_order_1 = user_data.order_set.filter(status=1).count()  # 待支付订单那数
    user_order_2 = user_data.order_set.filter(status=2).count()  # 已发货订单数

    content = {
        'type_list': gettypeall,
        'user_data': user_data,
        'user_order_1': user_order_1,
        'user_order_2': user_order_2,
    }
    return render(request, 'home/user_homepage.html', content)



# 修改用户信息
class UpdateUserInfo(View):
    def get(self, request):
        res = request.session.get('login_users').get('user_id')
        user_data = Users.objects.get(id=res)  # 查找用户信息
        content = {
            'user_data': user_data,
            'type_list': gettypeall,
        }
        return render(request, 'home/update_user_info.html', content)

    def post(self, request):
        from django.contrib.auth.hashers import make_password
        res = request.POST
        try:
            uname = request.session['login_users']['username']
            print(uname)
            user_a = Users.objects.exclude(delete_data=0).filter(id=res['id'])[0]
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
                raise AttributeError("年龄字段 修改 error , 修改 价值不是男或女, %s" % a)
            print(MYADMAIN_USER_V1)
            if request.FILES.get('pic', None):
                fil = filesload(request, 'pic', './static/public/pics/')
                user_a.pic = fil
            user_a.save()
            return HttpResponse('<script>alert("修改成功");location.href="/user_homepage/"</script>')
        except AttributeError as arterror:
            return HttpResponse('<script>alert("修改失败, 图片上传错误, 请重新修改");location.href="/update_user_info/"</script>')
        except BaseException as be:
            return HttpResponse('<script>alert("修改失败, 字段指定错误请重新修改");location.href="/update_user_info/"</script>')



