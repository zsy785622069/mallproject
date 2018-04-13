# myadmin --> urls.py
from django.conf.urls import url
from . import views

urlpatterns = [
    # 后台管理主页
    url(r'^$', views.index, name='myadminindex'),
    # 会员添加
    url(r'^useradd$', views.useradd, name='myadmin_useradd'),
    #   会员添加进数据库
    url(r'^user_insert$', views.user_insert, name='myadmin_user_insert'),
    #   会员删除
    url(r'^user_data_delele/(?P<uid>[0-9]+)$', views.user_data_delele, name='myadmin_user_data_delele'),

]
