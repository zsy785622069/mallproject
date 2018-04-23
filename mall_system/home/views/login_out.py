from django.shortcuts import render, redirect, reverse, HttpResponse
from django.views import View
from myadmin.models import Users

# 用户登录
class Login(View):
    def get(self,request):
        return render(request,'home/login.html')

    def post(self,request):
        from django.contrib.auth.hashers import check_password
        uname = request.POST.get('home_login_username')
        pwd = request.POST.get('home_login_password')
        try:
            # 筛选出非禁用帐号中, 用户登录的帐号
            users_data = Users.objects.exclude(status=0).filter(username=uname)[0]
            if users_data and check_password(pwd, users_data.password):
                request.session['login_status'] = True
                request.session['login_users'] = {'user_id': users_data.id, 'username': users_data.username}
                return redirect(reverse('home_index'))
        except:
            pass
        return HttpResponse('<script>alert("用户名或密码错误");location.href="/login/"</script>')


# 退出登录
def logout(request):
    request.session.flush()
    return redirect(reverse('home_index'))


# 用户注册
class Register(View):
    def get(self,request):
        return render(request,'home/register.html')

    def post(self,request):
        try:
            from django.contrib.auth.hashers import make_password
            res = request.POST
            list1 = ['username', 'password', 'phone', 'email', 'address', 'age', 'sex']
            for i in list1:
                if not res.get(i):
                    print(res.get(i))
                    return HttpResponse('<script>alert("字段为空, 无法添加");location.href="/register/"</script>')
            print('username_res',res.get('username'))
            users_name = Users.objects.filter(username=res.get('username'))
            print(users_name)
            if len(users_name) != 0:
                return HttpResponse('<script>alert("用户名已存在, 请重新添加");location.href="/register/"</script>')

            user_a = Users()
            user_a.username = res['username']
            user_a.password = make_password(res['password'], None, 'pbkdf2_sha256')
            user_a.phone = res['phone']
            user_a.email = res['email']
            user_a.address = res['address']
            user_a.age = res['age']
            user_a.sex = res['sex']
            user_a.status = 1
            user_a.save()
            request.session['login_status'] = True
            request.session['login_users'] = {'user_id': user_a.id, 'username': user_a.username}
        except:
            return HttpResponse('<script>alert("表单信息不正确, 请重新添加");location.href="/register/"</script>')
        return redirect(reverse('home_index'))














