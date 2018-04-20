#!/usr/bin/env python3
# from django.shortcuts import render
from django.http import HttpResponse
import re

class AdminLoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):

        # 检测当前的请求是否已经登录,如果已经登录,.则放行,如果未登录,则跳转到登录页
        # 获取当前用户的请求路径  /myadmin/login开头  但不是 /admin/login/  /admin/dologin/   /admin/verifycode
        urllist = ['/myadmin/login','/myadmin/verifycode']
        # 判断是否进入了后台,并且不是进入登录页面
        if re.match('/myadmin/',request.path) and request.path not in urllist:

            # 检测session中是否存在 adminlogin的数据记录
            if request.session.get('Admin_login',False) != True:
                # 如果在session没有记录,则证明没有登录,跳转到登录页面
                return HttpResponse('<script>alert("请先登录");location.href="/myadmin/login";</script>')

        # 用户主页 登录
        home_allow_login = ['/orderadd/', '/ordercreate/', '/buy/', '/myorder/', '/users_index/']
        if request.path in home_allow_login:
            if not request.session.get('login_status'):
                return HttpResponse('<script>alert("请先登录");location.href="/login/";</script>')

        response = self.get_response(request)
        return response



