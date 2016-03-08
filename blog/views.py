#-*- coding:utf-8 -*-
from django.shortcuts import render
from blog.models import Article, Tag, Classification,User  #导入创建的模型
from django import forms
from django.shortcuts import render_to_response,get_object_or_404
from django.core.paginator import Paginator,InvalidPage,EmptyPage,PageNotAnInteger
from django.template import RequestContext
from django.http import Http404
from haystack.forms import SearchForm
from django.contrib.auth.models import User  
from django.contrib import auth   
from django.db.models import Q
from django.template import loader,Context
from django.http import HttpResponse
#从Article、Tag、Classification中获取了所有的blog对象、tag对象和classification对象；           
def blog_list(request):
    blogs = Article.objects.all().order_by('-publish_time')
#调用了render_to_response方法，它的第一个参数是要使用的模板名称；第二个参数是为该模板创建 Context 时所使用的字典，可以理解为要传入模板的参数；而RequestContext默认地在模板context中加入了一些变量，如HttpRequest对象或当前登录用户的相关信息。
               
    return render_to_response('index.html', {"blogs": blogs}, context_instance=RequestContext(request))
def index(request):
    articles = Article.objects.all()
    page_size=2
    paginator = Paginator(articles, page_size)
    try:
        page = int(request.GET.get('page','1'))
    except ValueError:
        page = 1
        print page
    try:
        posts = paginator.page(page)
    except (EmptyPage, InvalidPage):
        posts = paginator.page(paginator.num_pages) 
    classification = Classification.objects.order_by('-id') 
    return render_to_response('blog/index.html',
                  locals(),
                  context_instance=RequestContext(request))
    
def content(request, id):
    article = get_object_or_404(Article, id=id)
    classification = Classification.objects.order_by('-id')
#    classification = Classification.objects.all()
    return render_to_response('blog/content.html',
                  locals(),
                  context_instance=RequestContext(request))
#def classification(request,id):
#    try:
#        cate = Classification.objects.get(id=id)  #点击分类，进入分类列表
#    except Classification.DoesNotExist:
#        raise Http404
#    articles_1 = Article.objects.filter(classification=cate) #外键匹配
#    is_category = True #如果该分类下存在文章
#    classification = Classification.objects.all() #取得所有文章
#    return render_to_response('blog/index.html',
#                              locals(),
#                    context_instance=RequestContext(request))
    
#    categorys = Classification.objects.order_by('-id') #分类文章的数目
#    articles = Article.objects.all()     #分类文章的数目
   
    # 计算每类的文章数目
#    for category in categorys:
#        category.article_num = 0
#        for article in articles:
#            if article.classification == category:
#               category.article_num += 1
#        category.save()
    
#    return categorys 
    
def classification(request,id):
    try:
        cate = Classification.objects.get(id=id)
    except Classification.DoesNotExist:
        raise Http404
    articles = Article.objects.filter(classification=cate)
    is_category = True
    classification = Classification.objects.all()
    return render_to_response('blog/index.html',
                              locals(),
                    context_instance=RequestContext(request))
#博文目录
def article_list(request):
 
    categorys = classification(request)
    keywords = request.GET.get('keywords')
    cate = request.GET.get('category')
     
    #根据搜索、分类和默认确定对应的文章
    if keywords:
        articles = Article.objects.order_by('-id').filter(Q(caption__icontains=keywords) | Q(content__icontains=keywords))    
    elif cate:
        articles = Article.objects.order_by('-id').filter(category__id=int(cate))            
    else:
        articles = Article.objects.order_by('-id')   
     
    #分页
    paginator = Paginator(articles,20)
     
    #确定某页的文章
    try:
        page = int(request.GET.get('page',1))
        if page < 1:
            page = 1
    except ValueError:
        page = 1   
     
    try:
        articlelist = paginator.page(page)
    except(EmptyPage,InvalidPage,PageNotAnInteger):
        articlelist = paginator.page(1)
 
    #页数太多时，页数范围确定为当前页码的前后几页 
    after_range_num = 3
    before_range_num = 2
     
    if page >= after_range_num:
        page_range = paginator.page_range[page - after_range_num:page + before_range_num]
    else:
        page_range = paginator.page_range[0:page + before_range_num]
 
    return render_to_response('blog/_article.html',locals())    
def full_search(request):
    """全局搜索"""
    keywords = request.GET['q']
    sform = SearchForm(request.GET)
    posts = sform.search()
    return render(request, 'blog/post_search_list.html',
                {'posts': posts, 'list_header': '关键字 \'{}\' 搜索结果'.format(keywords)})

class UserForm(forms.Form):
    username = forms.CharField(label='用户名：',max_length=100)
    passworld = forms.CharField(label='密码：',widget=forms.PasswordInput())
    email = forms.EmailField(label='电子邮件：')

# Create your views here.
def register(request):
    if request.method == "POST":
        uf = UserForm(request.POST)
        if uf.is_valid():
            #获取表单信息
            username = uf.cleaned_data['username']
            passworld = uf.cleaned_data['passworld']
            email = uf.cleaned_data['email']
            #将表单写入数据库
            user = User()
            user.username = username
            user.passworld = passworld
            user.email = email
            user.save()
            #返回注册成功页面
            return render_to_response('blog/success.html',{'username':username})
    else:
        uf = UserForm()
    return render_to_response('blog/register.html',{'uf':uf})

