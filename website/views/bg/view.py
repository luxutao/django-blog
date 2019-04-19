#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@__Create Time__ = 2017/12/29 下午5:00
@__Description__ = " "
"""
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView

from ...models import Article, Comment, Tag


# bg首页
class BackgroundIndexView(LoginRequiredMixin, TemplateView):
    template_name = 'bg/index.html'

    def get_context_data(self, **kwargs):
        context = super(BackgroundIndexView, self).get_context_data(**kwargs)
        context.update({
            'tags': Tag.objects.count(),
            'article_publish': Article.objects.filter(status=True).count(),
            'article_draft': Article.objects.filter(status=False).count(),
            'comment': Comment.objects.count()
        })
        return context
