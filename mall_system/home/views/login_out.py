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

# 用户注册
class Register(View):
    def get(self,request):
        return render(request,'home/register.html')

    def post(self,request):
        return redirect(reverse('home_index'))

# 退出登录
def logout(request):
    request.session.flush()
    return redirect(reverse('home_index'))
