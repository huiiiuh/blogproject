# -*- coding: utf-8 -*-
__author__ = 'hui'
__date__ = '2018/6/17 16:41'

from django.conf.urls import url
from . import views

app_name = 'comments'

urlpatterns = [
    url(r'^comment/post/(?P<post_pk>[0-9]+)/$', views.post_comment, name='post_comment'),
]