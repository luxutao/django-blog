#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@__Create Time__ = 2017/12/11 15:34
@__Description__ = " "
"""

import datetime
import os

from django import forms
from django.utils.translation import ugettext_lazy as _

from ..models import Article, Comment, Illustration, Tag


class TagModelMultipleChoiceField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return obj.showname


# 添加文章
class PublishArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            'title',
            'subtitle',
            'content',
            'status',
            'tag'
        ]
        labels = {
            'title': _('标题'),
            'subtitle': _('副标题'),
            'content': _('内容'),
            'status': _('操作状态'),
        }
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'subtitle': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
            }),
            'status': forms.Select(choices=(
                (True, '发布'),
                (False, '草稿')
            )),
        }
        error_messages = {
            'title': {
                'unique': _("标题已存在！"),
            },
        }
        help_texts = {
            'title': _('Please enter the title of the article here.'),
            'subtitle': _('Please enter the subtitle of the article here.'),
            'content': _('Please enter the content of the article here.'),
        }

    tag = TagModelMultipleChoiceField(
        label='标签',
        queryset=Tag.objects,
        to_field_name='id',
        widget=forms.CheckboxSelectMultiple(),
        help_text=_('Please choice the tags of the article here.')
    )


# 添加评论
class PublishCommentForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.object = kwargs.pop('object')
        self.floor = kwargs.pop('floor')
        self.avatar_url = kwargs.pop('avatar_url')
        super(PublishCommentForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Comment
        fields = [
            'email',
            'name',
            'content',
        ]
        labels = {
            'email': _('邮箱地址'),
            'name': _('名称'),
            'content': _('内容'),
        }
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control'
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
            }),
        }

    def save(self, commit=True):
        self.instance.floor = self.floor
        self.instance.article = self.object
        self.instance.avatar_url = self.avatar_url
        if commit:
            self.instance.save()
        return self.instance


# 添加插图
class IllustrationForm(forms.ModelForm):
    class Meta:
        model = Illustration
        fields = ['file']
        labels = {
            'file': _('上传图片')
        }
        widgets = {
            'file': forms.FileInput
        }

    def save(self, commit=True):
        filename, suffix = os.path.splitext(self.instance.file.name)
        self.instance.file.name = datetime.datetime.now().strftime('%Y%m%d%H%M%S') + suffix
        if commit:
            self.instance.save()
        return self.instance
