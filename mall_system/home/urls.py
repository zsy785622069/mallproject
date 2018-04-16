# home --> urls

from django.conf.urls import url
from home.views import home_views, list_views

urlpatterns = [
    # 1. 商城首页
    url(r'^$', home_views.index, name='home_index'),
    url(r'^index.html$', home_views.index, name='home_index'),
    # 2. 列表页
    url(r'^list$', list_views.list_index_all, name='home_list_all'),
    url(r'^list.html$', list_views.list_index_all),
    url(r'^list(?P<type_id>[0-9]+)$', list_views.list_index, name='home_list'),
]
