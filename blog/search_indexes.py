#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from models import Article
from haystack import indexes
#创建博客索引
class ArticleIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    # 对caption字段进行索引
    caption = indexes.CharField(model_attr='caption')
    def get_model(self):
        return Article

    def index_queryset(self, using=None):
        return self.get_model().objects.all() #确定在建立索引时有些记录被索引，这里我们简单地返回所有记录  