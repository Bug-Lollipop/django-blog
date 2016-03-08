from django.conf.urls import patterns,url
urlpatterns = patterns('',
        url(r'^$','blog.views.index'),
        url(r'^article/(?P<id>\d+)/$','blog.views.content'),
        url(r'category/(?P<id>\d+)/$','blog.views.classification'),
        url(r'^article-list/$', 'blog.views.article_list'),
#        url(r'^comments/','django_comments.urls'), 
      
 #       url(r'^blog/register/$','blog.views.register'),
       
       
)