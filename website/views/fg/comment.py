#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@__Create Time__ = 2017/12/15 下午2:41
@__Description__ = " "
"""

import os
import random

from django.urls import reverse
from django.views.generic import CreateView

from blog.settings import BASE_DIR
from ...forms.edit import PublishCommentForm
from ...models import Article


# 添加评论
class PublishCommentView(CreateView):
    template_name = 'fg/detail.html'
    form_class = PublishCommentForm

    def dispatch(self, request, *args, **kwargs):
        self.request = self.request
        return super(PublishCommentView, self).dispatch(request, *args, **kwargs)

    # 通过路径获得文章对象
    def get_article(self):
        article = Article.objects.get(pk=int(self.request.path.split('/')[-1]))
        return article

    def get_floor(self, object):
        queryset = object.website_comment_related.all().order_by('-id')
        if not queryset:
            return 0
        return int(queryset[0].floor)

    # 添加form的数据
    def get_form_kwargs(self):
        kwargs = super(PublishCommentView, self).get_form_kwargs()
        kwargs.update({
            'floor': self.get_floor(self.get_article()) + 1,
            'object': self.get_article(),
            'avatar_url': self.get_avatar_url()
        })
        return kwargs

    # 获得随机的头像
    def get_avatar_url(self):
        filenames = [os.path.basename(file) for file in os.listdir(BASE_DIR + '/website/static/img/comment/')]
        return '/static/img/comment/' + random.choice(filenames)

    def get_success_url(self):
        success_url = reverse(viewname='fg_article_detail', args=(self.get_article().id,))
        return success_url
