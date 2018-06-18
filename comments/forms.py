# -*- coding: utf-8 -*-
__author__ = 'hui'
__date__ = '2018/6/17 16:09'
from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'url', 'text']