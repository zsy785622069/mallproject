from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.views import View
from my_public_package.my_models import ramdom_num
from myadmin.models import Users

class Login(View):
    def get(self, request):
        res_sess = request.session.get('login_error','')
        request.session['login_error'] = ''
        return render(request, 'myadmin/login_out/login.html', {'error': res_sess})

    def post(self, request):
        from django.contrib.auth.hashers import check_password

        if request.session.get('verifycode').lower() != request.POST.get('vcode').lower():
            request.session['login_error'] = '验证码错误'
            return redirect(reverse('myadmin_login'))
        ob = Users.objects.filter(status=2).filter(username=request.POST.get('username'))
        print(ob)
        for i in ob:
            if request.POST.get('username') == i.username and check_password(request.POST.get('password'), i.password):
                print(request.POST.get('username') == i.username)
                print(check_password(request.POST.get('password'), i.password))
                request.session['Admin_login'] = True
                request.session['user_name'] = i.username
                request.session['user_id'] = i.id
                request.session['user_pic'] = i.pic
                return redirect(reverse('myadminindex'))

        request.session['login_error'] = '帐号或密码错误'
        return redirect(reverse('myadmin_login'))

def logout(request):
    request.session.flush()
    return redirect(reverse('myadmin_login'))


# 验证码
def verifycode(request):
    #引入绘图模块
    from PIL import Image, ImageDraw, ImageFont
    #引入随机函数模块
    import random
    #定义变量，用于画面的背景色、宽、高
    bgcolor = (random.randrange(20, 100), random.randrange(20, 100), 255)
    width = 120
    height = 40
    #创建画面对象
    im = Image.new('RGB', (width, height), bgcolor)
    #创建画笔对象
    draw = ImageDraw.Draw(im)
    #调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    rand_str = ramdom_num(6)
    #构造字体对象
    font = ImageFont.truetype('NotoSansCJK-Light.ttc', 23)
    #构造字体颜色
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    #绘制4个字
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
    draw.text((40, 2), rand_str[2], font=font, fill=fontcolor)
    draw.text((65, 2), rand_str[3], font=font, fill=fontcolor)
    draw.text((80, 2), rand_str[4], font=font, fill=fontcolor)
    draw.text((100, 2), rand_str[5], font=font, fill=fontcolor)
    #释放画笔
    del draw
    #存入session，用于做进一步验证
    request.session['verifycode'] = rand_str
    import io
    buf = io.BytesIO()
    #将图片保存在内存中，文件类型为png
    im.save(buf, 'png')
    #将内存中的图片数据返回给客户端，MIME类型为图片 png
    return HttpResponse(buf.getvalue(), 'image/png')





