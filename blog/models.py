from django.contrib.auth.models import User
from django.db import models
from django.utils.six import python_2_unicode_compatible
from django.urls import reverse


# python_2_unicode_compatible 装饰器用于兼容 Python2
@python_2_unicode_compatible
class Category(models.Model):
    '''
    分类
    '''
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Tag(models.Model):
    '''
    标签
    '''
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Post(models.Model):
    '''
    文章
    '''
    # 文章标题
    title = models.CharField(max_length=70)
    # 文章正文
    body = models.TextField()

    visiting = models.PositiveIntegerField(default=0)

    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()

    # 文章摘要, 允许为空值
    excerpt = models.CharField(max_length=200, blank=True)

    # 一篇文章只能对应一个分类，一个分类下可以有多篇文章，使用的是 ForeignKey，即一对多的关联关系。
    category = models.ForeignKey(Category)
    # 一篇文章可以有多个标签，同一个标签下也可能有多篇文章，使用 ManyToManyField，表明这是多对多的关联关系。
    tag = models.ManyToManyField(Tag, blank=True)

    # 文章作者
    author = models.ForeignKey(User)

    def __str__(self):
        return self.title

    # 自定义 get_absolute_url 方法
    # 记得从 django.urls 中导入 reverse 函数
    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    def increase_visiting(self):
        # 访问量+1
        self.visiting += 1
        self.save(update_fields=['visiting']) # #只保存某个字段

    class Meta:
        ordering = ['-created_time']





























