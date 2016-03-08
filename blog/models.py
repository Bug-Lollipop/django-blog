#-*- coding:utf-8 -*-
from django.db import models
from django.contrib import admin
# 插入数据：new_blog = Article(caption='my blog title', author='author', classification='classification', content = 'blog content')

# 保存数据：new_blog.save()

# 获取数据 / 更新数据：id = new_blog.id / new_blog.caption = 'new title'

# 选择表中的所有对象：blogs = Article.objects.all()

# 过滤数据：specified_blogs = Article.objects.filter(classification='classification')

# 获取单个对象：blog = Article.objects.get(name='my blog title')

# 排序：blogs = Article.objects.order_by('name')

# 删除数据：blog.delete()
#便签   
#标签名、创建时间     
class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField()
class UserAdmin(admin.ModelAdmin):
    list_display = ('username','email')
    
admin.site.register(User,UserAdmin)

class Tag(models.Model):
    tag_name = models.CharField(max_length=20)
    create_time = models.DateTimeField(auto_now_add=True)
            
    def __unicode__(self):
        return self.tag_name
#分类    
#分类名称        
class Classification(models.Model):
    name = models.CharField(max_length=20)
    article_num = models.IntegerField(default=0)        
    def __unicode__(self):
        return u'%s' % self.name
#作者       
#包括姓名、邮箱、网站     
class Author(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(blank=True)
    website = models.URLField(blank=True)
            
    def __unicode__(self):
        return u'%s' % (self.name)
#文章 
#包括标题、副标题、发布时间、更新时间、作者、文章分类、标签、正文           
class Article(models.Model):
    caption = models.CharField(u'标题',max_length=30)
    subcaption = models.CharField(u'副标题',max_length=50, blank=True)
    publish_time = models.DateTimeField(u'发布时间',auto_now_add=True)
    update_time = models.DateTimeField(u'更新时间',auto_now=True)
    author = models.ForeignKey(Author)
    classification = models.ForeignKey(Classification)
    tags = models.ManyToManyField(Tag, blank=True)
    content = models.TextField(u'正文',)
    def __unicode__(self):  
        return self.caption  