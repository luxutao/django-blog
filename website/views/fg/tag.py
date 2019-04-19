#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@__Create Time__ = 2017/12/25 上午9:54
@__Description__ = " "
"""

import random

from django.views.generic import ListView

from ...models import Tag, Article


# 前端查看标签和文章
class FrontEndTagArticleView(ListView):
    template_name = 'fg/articleOne.html'
    model = Article
    paginate_by = 10

    def dispatch(self, request, *args, **kwargs):
        # 获得筛选条件值
        self.filter = request.GET.get('filter', None)
        return super(FrontEndTagArticleView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(FrontEndTagArticleView, self).get_context_data(**kwargs)
        tag_list, color = self.randomColor()
        if self.filter is not None:
            page = self.filter
        else:
            page = False
        context.update({
            'tag_list': zip(tag_list, color),
            'page': page
        })
        return context

    def get_queryset(self):
        if self.filter is not None:
            queryset = Tag.objects.get(valuename=self.filter).website_article_related.filter(status=True)
        else:
            queryset = Article.objects.filter(status=True)

        return queryset

    # 标签随机背景色
    def randomColor(self):
        tag_list = Tag.objects.all()
        color = [[random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)] for _ in
                 range(0, tag_list.count())]
        return tag_list, color


# 前端查看标签和文章（第二种模式)
class FrontEndTagArticleLoadView(ListView):
    template_name = 'fg/articleTwo.html'
    model = Tag

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(FrontEndTagArticleLoadView, self).get_context_data(**kwargs)
        tag_list, color = self.randomColor()
        context.update({
            'tag_list': zip(tag_list, color),
        })
        return context

    def randomColor(self):
        tag_list = self.model.objects.all()
        color = [[random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)] for _ in
                 range(0, tag_list.count())]
        return tag_list, color
