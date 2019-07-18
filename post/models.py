# encoding: UTF-8
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
from django.db import models
from ckeditor.fields import RichTextField

class Category(models.Model):
    """分类"""
    name = models.CharField(max_length=100)


class Tag(models.Model):
    """标签"""
    name = models.CharField(max_length=100)


class Post(models.Model):
    """文章"""
    objects = models.Manager()
    title = models.CharField(max_length=100)
    body = RichTextField('正文')
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    excerpt = models.CharField(max_length=200, blank=True)  # 文章摘要，可为空
    category = models.ForeignKey(Category, on_delete=True)  # ForeignKey表示1对多（多个post对应1个category）
    tags = models.ManyToManyField(Tag, blank=True)
    views = models.PositiveIntegerField(default=0)  # 阅读量




