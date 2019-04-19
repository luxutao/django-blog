#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@__Create Time__ = 2017/12/11 10:34
@__Description__ = " "
"""

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.urls.base import reverse_lazy
from django.views.generic.base import View
from django.views.generic.edit import CreateView, UpdateView, BaseDeleteView
from django.views.generic.list import ListView

from ...forms.edit import PublishArticleForm
from ...models import Article, Tag


# 添加一篇文章
class PublishArticleView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'bg/publish.html'
    success_url = reverse_lazy('bg_article_publish')

    # 将文章与标签绑定
    def form_valid(self, form):
        article = form.save(True)
        default = Tag.objects.get(pk=1)
        for tag in form.cleaned_data['tag']:
            article.tag.add(tag)
        article.tag.add(default)
        article.save()
        return super(PublishArticleView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, form.errors.as_text())
        return super(PublishArticleView, self).form_invalid(form)

    # 取消副标题的必须性
    def get_form(self, form_class=None):
        form = PublishArticleForm
        form_new = super(PublishArticleView, self).get_form(form)
        form_new.fields['subtitle'].required = False
        return form_new

    def get_success_message(self, cleaned_data):
        if cleaned_data['status'] is True:
            return '文章发表成功！'
        else:
            return '文章已存为草稿！'


# 删除一篇文章
class DeleteArticleView(LoginRequiredMixin, BaseDeleteView):
    model = Article
    success_url = reverse_lazy('bg_article_list')


# 编辑一篇文章
class EditArticleView(LoginRequiredMixin, UpdateView):
    model = Article
    template_name = 'bg/publish.html'
    form_class = PublishArticleForm
    success_url = reverse_lazy('bg_article_list')

    def get_initial(self):
        return {
            'content': self.object.content,
            'title': self.object.title,
            'subtitle': self.object.subtitle,
            'status': self.object.status
        }

    def get_context_data(self, **kwargs):
        context = super(EditArticleView, self).get_context_data(**kwargs)
        context.update({
            'initial': self.object.content,
            'article': self.object
        })
        return context


# 后台文章列表
class ArticleListView(LoginRequiredMixin, ListView):
    model = Article
    queryset = Article.objects.all()
    template_name = 'bg/article.html'
    paginate_by = 10


# 搜索文章
class SearchArticleView(LoginRequiredMixin, ListView):
    template_name = 'bg/article.html'
    paginate_by = 10

    def dispatch(self, request, *args, **kwargs):
        if request.method == 'GET':
            self.word = request.GET.get('word')
        return super(SearchArticleView, self).dispatch(request, *args, **kwargs)

    # 类似模糊搜索
    def get_queryset(self):
        queryset = Article.objects.filter(
            Q(title__contains=self.word) | Q(subtitle__contains=self.word) | Q(content__contains=self.word)
        )
        return queryset


# 多选操作
class MultipleSelectionSettingView(LoginRequiredMixin, View):

    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            handle = request.POST.get('handle')
            article = request.POST.getlist('article')
            queryset = Article.objects.filter(id__in=article)
            if handle == 'delete':
                queryset.delete()
            if handle == 'publish':
                queryset.update(status=True)
            if handle == 'draft':
                queryset.update(status=False)
            return HttpResponseRedirect(reverse_lazy('bg_article_list'))

        return super(MultipleSelectionSettingView, self).dispatch(request, *args, **kwargs)
