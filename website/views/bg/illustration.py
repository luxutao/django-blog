#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@__Create Time__ = 17-12-15 下午11:47
@__Description__ = " "
"""

import os

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.edit import BaseDeleteView

from blog.settings import BASE_DIR
from ...forms.edit import IllustrationForm
from ...models import Illustration


# 插入一张图片
class IllustrationView(LoginRequiredMixin, CreateView):
    form_class = IllustrationForm
    template_name = 'bg/illustration.html'
    success_url = reverse_lazy('bg_illustration')

    def form_valid(self, form):
        return super(IllustrationView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(IllustrationView, self).get_context_data(**kwargs)
        context.update({
            # 倒序方式显示
            'illustration_list': Illustration.objects.order_by('-id')
        })
        return context


# 删除一张图片
class DeleteIllustrationView(LoginRequiredMixin, BaseDeleteView):
    model = Illustration

    def get_success_url(self):
        os.remove(BASE_DIR + '/website' + self.object.file.url)
        return reverse_lazy('bg_illustration')
