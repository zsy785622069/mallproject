#!/usr/bin/env python3
from django import template
register = template.Library()

# 标签
@register.filter
def jia(a):
    res = a.count(',')
    return res

# 过滤器
@register.simple_tag
def kong_upper(id, val):
    res = id.count(',') - 1
    va = ' |---- '*res + val
    return va


# 标签
# @register.simple_tag
# def jia(a):
#     res = a.count(',')
#     return res

# 过滤器
# @register.filter
# def kong_upper(val):
#     print ('val from template:',val)
#     return val