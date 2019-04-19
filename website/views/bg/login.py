#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@__Create Time__ = 2017/12/11 11:08
@__Description__ = " "
"""

from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.urls.base import reverse_lazy

from ...forms.login import LoginAuthForm


# user login
class UserLoginView(LoginView):
    template_name = 'bg/login.html'

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super(UserLoginView, self).dispatch(request, *args, **kwargs)

    def get_form(self, form_class=None):
        form = LoginAuthForm
        form_new = super(UserLoginView, self).get_form(form)
        form_new.fields['remember'].required = False
        return form_new

    def form_valid(self, form):
        if form.cleaned_data.get('remember') is False:
            self.request.session.set_expiry(7200)
        else:
            self.request.session.set_expiry(259200)
        return super(UserLoginView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, form.errors.as_text())
        return super(UserLoginView, self).form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('bg_index')


# user logout
class UserLogoutView(LogoutView):
    template_name = 'bg/logout.html'
