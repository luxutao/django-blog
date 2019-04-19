#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@__Create Time__ = 2017/12/15 下午4:29
@__Description__ = " "
"""

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import BaseDeleteView

from ...models import Comment


# 评论列表
class CommentListView(LoginRequiredMixin, ListView):
    template_name = 'bg/comment.html'
    model = Comment
    paginate_by = 10


# 删除评论
class DeleteCommentView(LoginRequiredMixin, BaseDeleteView):
    model = Comment
    success_url = reverse_lazy('bg_comment_list')
