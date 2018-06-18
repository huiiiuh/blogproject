from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

import markdown, pygments
from comments.forms import CommentForm

from .models import Post, Category


def index(request):
    '''
    首页
    '''
    post_list = Post.objects.all()
    return render(request, 'blog/index.html', context={
        'post_list': post_list
    })


def detail(request, pk):
    '''
    详情页
    '''
    post = get_object_or_404(Post, pk=pk)
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite', # 语法高亮拓展
                                      'markdown.extensions.toc', # 自动生成目录
                                  ])
    post.increase_visiting()

    comment_form = CommentForm()
    comment_list = post.comment_set.all()

    # 将文章、表单、以及文章下的评论列表作为模板变量传给 detail.html 模板，以便渲染相应数据。
    return render(request, 'blog/detail.html', context={
        'post': post,
        'comment_form': comment_form,
        'comment_list': comment_list,
    })


def archives(request, year, month):
    '''
    归档
    '''
    post_list = Post.objects.filter(created_time__year=year, created_time__month=month)
    return render(request, 'blog/index.html', context={'post_list': post_list})


def category(request, pk):
    '''
    分类
    '''
    cat = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cat)
    return render(request, 'blog/index.html', context={'post_list': post_list})