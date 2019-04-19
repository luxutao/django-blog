"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from website.views.bg import *
from website.views.fg import article as fg_article
from website.views.fg import comment as fg_comment
from website.views.fg import tag as fg_tag
from website.views.fg import view as fg_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # 后台管理页面
    url(r'^bg/index$', view.BackgroundIndexView.as_view(), name='bg_index'),
    url(r'^bg/login$', login.UserLoginView.as_view(), name='bg_login'),
    url(r'^bg/logout$', login.UserLogoutView.as_view(), name='bg_logout'),
    url(r'^bg/article/publish$', article.PublishArticleView.as_view(), name='bg_article_publish'),
    url(r'^bg/article$', article.ArticleListView.as_view(), name='bg_article_list'),
    url(r'^bg/article/delete/(?P<pk>[0-9]+)$', article.DeleteArticleView.as_view(), name='bg_article_delete'),
    url(r'^bg/article/edit/(?P<pk>[0-9]+)$', article.EditArticleView.as_view(), name='bg_article_edit'),
    url(r'^bg/article/search$', article.SearchArticleView.as_view(), name='bg_article_search'),
    url(r'^bg/article/multiple$', article.MultipleSelectionSettingView.as_view(), name='bg_article_multiple'),
    url(r'^bg/comment$', comment.CommentListView.as_view(), name='bg_comment_list'),
    url(r'^bg/comment/delete/(?P<pk>[0-9]+)$', comment.DeleteCommentView.as_view(), name='bg_comment_delete'),
    url(r'^bg/illustration$', illustration.IllustrationView.as_view(), name='bg_illustration'),
    url(r'^bg/illustration/delete/(?P<pk>[0-9]+)$', illustration.DeleteIllustrationView.as_view(),
        name='bg_illustration_delete'),

    url(r'^bg/tag$', tag.TagView.as_view(), name='bg_tag'),
    url(r'^bg/tag/create$', tag.CreateTagView.as_view(), name='bg_tag_create'),
    url(r'^bg/tag/edit/(?P<pk>[0-9]+)$', tag.EditTagView.as_view(), name='bg_tag_edit'),
    url(r'^bg/tag/delete/(?P<pk>[0-9]+)$', tag.DeleteTagView.as_view(), name='bg_tag_delete'),
    # 查询标签下的文章
    url(r'^bg/tag/dr$', tag.BackgroundTagArticleView.as_view(), name='bg_tta'),

    # 前端标签页的两种模式
    url(r'^fg/tag/modelOne$', fg_tag.FrontEndTagArticleView.as_view(), name='fg_tta_one'),
    url(r'^fg/tag/modelTwo$', fg_tag.FrontEndTagArticleLoadView.as_view(), name='fg_tta_two'),

    # 前端显示页面
    url(r'^index$', fg_view.IndexView.as_view(), name='index'),
    url(r'^$', fg_view.IndexView.as_view()),
    url(r'^about$', fg_view.AboutView.as_view(), name='about'),
    url(r'^detail/(?P<pk>[0-9]+)$', fg_article.DetailArticleView.as_view(), name='fg_article_detail'),
    url(r'^comment/(?P<pk>[0-9]+)$', fg_comment.PublishCommentView.as_view(), name='fg_publish_comment'),

]
