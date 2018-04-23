# home --> urls

from django.conf.urls import url
from home.views import home_views, list_views,detail_views,cart_views, login_out, users_order,user_homepage

urlpatterns = [
    # 1. 商城首页
    url(r'^$', home_views.index, name='home_index'),
    url(r'^index.html$', home_views.index, name='home_index_html'),
    # 2. 列表页
    url(r'^list$', list_views.list_index_all, name='home_list_all'),
    url(r'^list.html$', list_views.list_index_all, name='home_list_index'),
    url(r'^list(?P<type_id>[0-9]+)$', list_views.list_index, name='home_list'),
    # 3. 详情页 detail
    url(r'^detail-(?P<goods_id>[0-9]+)$', detail_views.detail_index, name='home_detail'),

    # 4. 购物车
    # url(r'^cart', cart_views.CartIndex.as_view(), name='home_cart'),
    #   4.1. 购物车商品添加
    url(r'^cart$', cart_views.CartIndex.as_view(), name='home_cart'),
    #   4.2. 清楚购物车
    url(r'^cart_clear$', cart_views.cart_clear, name='cart_clear'),
    #   4.3. 负责修改商品数量
    url(r'^cart_update$', cart_views.cart_update, name='cart_update'),
    #   4.4. 删除商品
    url(r'^cart_del$', cart_views.cart_del, name='cart_del'),

    # 登录
    url(r'^login/$', login_out.Login.as_view(), name='home_login'),
    # 退出
    url(r'^logout/$', login_out.logout, name='home_logout'),
    # 注册
    url(r'^register/$', login_out.Register.as_view(), name='home_register'),

    # 需要登录的 -------------------------
    # 提交订单
    url(r'^orderadd/$', users_order.OrederAdd.as_view(), name='home_orderadd'),

    # 订单创建
    url(r'^ordercreate/$', users_order.ordercreate, name='home_ordercreate'),

    # 支付
    url(r'^buy/(?P<oid>[0-9]+)$', users_order.buy, name='home_buy'),

    # 支付成功
    url(r'^pay/(?P<oid>[0-9]+)$', users_order.pay, name='home_pay'),

    # 用户订单
    url(r'^myorder/$', users_order.myorder, name='home_myorder'),

    # 用户主页
    url(r'^user_homepage/$', user_homepage.user_homepage, name='home_users_index'),

    # 更改用户信息
    url(r'^update_user_info/$', user_homepage.UpdateUserInfo.as_view(), name='update_user_info'),

]
