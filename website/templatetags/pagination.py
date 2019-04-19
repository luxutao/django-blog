#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@__Create Time__ = 2017/12/14 上午10:22
@__Description__ = " "
"""

from django import template

register = template.Library()


# 后台文章列表的分页器封装
@register.filter
def pagination(pages, crrent):
    if len(pages) <= 5:
        return pages
    else:
        index = pages.index(crrent)
        if index == 0 or index == 1 or index == 2:
            return pages[0:5]
        if index == len(pages) or index == len(pages) - 1 or index == len(pages) - 2:
            return pages[len(pages) - 5:len(pages)]
        else:
            return pages[index - 2:index + 3]
