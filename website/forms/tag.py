#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@__Create Time__ = 2017/12/25 上午9:56
@__Description__ = " "
"""

from django import forms
from django.utils.translation import ugettext_lazy as _

from ..models import Tag


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'
        labels = {
            'showname': _('显示名称'),
            'valuename': _('代替值名称'),
            'introduction': _('简介')
        }
        widgets = {
            'showname': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'valuename': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'introduction': forms.Textarea(attrs={
                'class': 'form-control',
            }),
        }
        error_messages = {
            'showname': {
                'unique': _("显示名称已存在！"),
            },
            'valuename': {
                'unique': _("代替值名称已存在！"),
            }
        }
        help_texts = {
            'showname': _('Please enter the showname of the tag here'),
            'valuename': _('Please enter the name value of the tag here'),
            'introduction': _('Please enter the introduction of the tag here'),
        }
