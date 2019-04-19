#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@__Create Time__ = 2017/12/25 上午9:54
@__Description__ = " "
"""

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView
from django.views.generic.edit import BaseCreateView, BaseDeleteView

from ...forms.tag import TagForm
from ...models import Tag


# 标签管理
class TagView(LoginRequiredMixin, ListView):
    model = Tag
    template_name = 'bg/tag.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TagView, self).get_context_data(**kwargs)
        context.update({
            'form': TagForm(),
        })
        return context


# 添加新标签
class CreateTagView(LoginRequiredMixin, BaseCreateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy('bg_tag')


# 编辑标签
class EditTagView(LoginRequiredMixin, UpdateView):
    model = Tag
    form_class = TagForm
    template_name = 'bg/tag.html'

    # 初始化form值
    def get_initial(self):
        return {
            'showname': self.object.showname,
            'valuename': self.object.valuename,
            'introduction': self.object.introduction
        }

    def get_context_data(self, **kwargs):
        context = super(EditTagView, self).get_context_data(**kwargs)
        context.update({
            'object_list': Tag.objects.all()
        })
        return context


# 删除标签
class DeleteTagView(LoginRequiredMixin, BaseDeleteView):
    model = Tag
    success_url = reverse_lazy('bg_tag')

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


# 后台查看标签下的文章
class BackgroundTagArticleView(LoginRequiredMixin, ListView):
    template_name = 'bg/article.html'
    paginate_by = 10
    model = Tag

    def dispatch(self, request, *args, **kwargs):
        self.filter = request.GET.get('filter')
        return super(BackgroundTagArticleView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        tag_object = self.model.objects.get(valuename=self.filter)
        return tag_object.website_article_related.all()
