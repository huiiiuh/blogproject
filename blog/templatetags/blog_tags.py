from django import template

from ..models import Post, Category

register = template.Library()


@register.simple_tag()
def get_recent_posts(num=5):
    '''
    获取最新5篇文章
    '''
    return Post.objects.all().order_by('-created_time')[:num]


@register.simple_tag()
def archives():
    '''
    归档
    '''
    # dates方法会返回一个列表，列表中的元素为每一篇文章（Post）的创建时间，且是 Python 的 date 对象，精确到月份，降序排列
    return Post.objects.dates('created_time', 'month', order='DESC')


@register.simple_tag()
def get_categories():
    '''
    分类
    '''
    return Category.objects.all()

