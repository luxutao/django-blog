#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@__Create Time__ = 2017/12/27 下午5:02
@__Description__ = " "
"""

from django.core.management.base import BaseCommand

from website.models import Tag


class Command(BaseCommand):
    def handle(self, *args, **options):
        Tag.objects.create(
            showname='默认的',
            valuename='default',
            introduction='默认的初始化标签，新添加文章都将默认勾选此标签。'
        )
