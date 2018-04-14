#!/usr/bin/env python3
from django import template
register = template.Library()

# 过滤器  {{ value|function }}
@register.filter
def jia(a):
    res = a.count(',')
    return res

# 标签  {% function value1 value2 %}
@register.simple_tag
def kong_upper(id, val):
    res = id.count(',') - 1
    va = ' |---- '*res + val
    return va

