#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@__Create Time__ = 2017/12/11 14:38
@__Description__ = " "
"""

from django.views.generic import DetailView

from ... import models


# 阅读页面
class DetailArticleView(DetailView):
    model = models.Article
    template_name = 'fg/detail.html'

    def get_context_data(self, **kwargs):
        context = super(DetailArticleView, self).get_context_data(**kwargs)
        context.update({
            'comment_object': self.object.website_comment_related.all()
        })
        return context

    # 每点击一次文章阅读次数加一
    def get_object(self, queryset=None):
        article = super(DetailArticleView, self).get_object(queryset)
        article.views += 1
        article.save()
        return article
