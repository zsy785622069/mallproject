#!/usr/bin/env python3
from django import template
register = template.Library()

# 标签  {% function value1 value2 %}
@register.filter
def num_com(val1, val2):
    return val1*val2

