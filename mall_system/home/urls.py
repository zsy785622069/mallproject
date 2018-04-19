# home --> urls

from django.conf.urls import url
from home.views import home_views, list_views,detail_views,cart_views

urlpatterns = [
    # 1. 商城首页
    url(r'^$', home_views.index, name='home_index'),
    url(r'^index.html$', home_views.index, name='home_index'),
    # 2. 列表页
    url(r'^list$', list_views.list_index_all, name='home_list_all'),
    url(r'^list.html$', list_views.list_index_all),
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

    # 登录, 注册,
    url(r'^detail-(?P<goods_id>[0-9]+)$', detail_views.detail_index, name='home_detail'),
]
