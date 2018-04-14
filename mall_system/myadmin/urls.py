# myadmin --> urls.py
from django.conf.urls import url
from myadmin.views import views, types_views, goods_views

urlpatterns = [
    # 用户首页
    url(r'^$', views.home, name='myadminhome'),

    # -----------------------------
    # 1. 后台管理主页
    url(r'^user_index$', views.index, name='myadminindex'),

    # -----------------------------
    #   1). 会员添加
    #       (1). 展示添加会员页面
    url(r'^useradd$', views.useradd, name='myadmin_useradd'),
    #       (2). 将用户添加的进入数据库
    url(r'^user_insert$', views.user_insert, name='myadmin_user_insert'),
    #   2). 会员删除
    url(r'^user_data_delele/(?P<uid>[0-9]+)$', views.user_data_delele, name='myadmin_user_data_delele'),
    #   3). 会员信息修改
    #       (1): 展示修改页面
    url(r'^user_data_update/(?P<us_id>[0-9]+)$', views.user_data_update, name='myadmin_user_data_update'),
    #       (2): 将用户修改的进入数据库
    url(r'^user_update_sql$', views.user_update_sql, name='myadmin_user_update_sql'),

    # -----------------------------
    # 2. 后台分类主页
    #   2.1. 分类管理列表
    url(r'^type_index$', types_views.type_index, name='myadmin_type_index'),
    #   2.2. 分类添加
    # url(r'^type_add$', types_views.type_add, name='myadmin_type_add'),
    url(r'^type_add$', types_views.TypeAdd.as_view(), name='myadmin_type_add'),
    #   2.3. 分类删除
    url(r'^type_del/(?P<del_id>[0-9]+)', types_views.type_del, name='myadmin_type_del'),
    #   2.4. 分类编辑
    url(r'^type_up_edit/(?P<up_id>[0-9]+)$', types_views.TypeUpdate.as_view(), name='myadmin_type_up_edit'),
    url(r'^type_update$', types_views.TypeUpdate.as_view(), name='myadmin_type_update'),

    # -----------------------------
    # 3. 商品主页
    #   3.1. 添加商品
    url(r'^goods_add$', goods_views.GoodsAdd.as_view(), name='myadmin_goods_add'),
    #   3.2. 展示商品信息
    url(r'^goods_index$', goods_views.goods_index, name='myadmin_goods_index'),

]
