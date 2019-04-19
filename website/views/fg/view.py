#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@__Create Time__ = 2017/12/11 14:38
@__Description__ = " "
"""

from django.views.generic import ListView, DetailView, TemplateView

from ... import models


# 前端首页
class IndexView(ListView):
    queryset = models.Article.objects.filter(status=True)
    template_name = 'fg/index.html'
    paginate_by = 6

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update({
            'tags': models.Tag.objects.all()
        })
        return context


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


# about
class AboutView(TemplateView):
    template_name = 'fg/about.html'

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context.update({
            'tags': models.Tag.objects.all()
        })
        return context
