#-*- coding:utf-8 -*-
"""
Django settings for mysite project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'a!kbx9%4()9%e)r)peu)wyz2@49=cy5#p0a3!u@n@@7r(r0ikt'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    #'grappelli.dashboard',  
    #'grappelli', #必须放在admin之前
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

#     other apps
     'markdown_deux',
     'haystack',
     'pagination',
#     my apps
     'blog',
    
)
#SITE_ID=1
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'pagination.middleware.PaginationMiddleware',#分页功能
#    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',   #中文转换
#     "django.contrib.messages.context_processors.messages"
 
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
)
ROOT_URLCONF = 'mysite.urls'

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATICFILES_DIRS = (
   os.path.join(os.path.dirname(__file__), 'static').replace('\\','/'),   #替换成自己的static 目录
)

STATIC_URL = '/mysite/static/'
#ADMIN_MEDIA_PREFIX = STATIC_URL + "grappelli/" 

TEMPLATE_DIRS = (
     os.path.join(os.path.dirname(__file__), 'templates').replace('\\','/'),
)
#TEMPLATE_CONTEXT_PROCESSORS = (
 #   "django.contrib.auth.context_processors.auth",
 #    'django.core.context_processors.debug',
 #   "django.core.context_processors.request",
 #   "django.core.context_processors.i18n",
 #    'django.core.context_processors.media',
 #   'django.contrib.messages.context_processors.messages',
#)
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_cn_backend.WhooshEngine',  
        'PATH': os.path.join(BASE_DIR, 'whoosh_index').replace('\\','/'),
    },
}
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'
#HAYSTACK_SITECONF = 'search_sites' #之前创建的文件名
#HAYSTACK_SEARCH_ENGINE = 'solr'
#HAYSTACK_SOLR_URL = 'http://127.0.0.1:8080/solr/'#solr所在服务器
#HAYSTACK_SOLR_TIMEOUT = 60 * 5
#HAYSTACK_INCLUDE_SPELLING = True
#HAYSTACK_BATCH_SIZE = 100
 
#HAYSTACK_CONNECTIONS = {
#    'default': {
#        'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
#        'URL': 'http://127.0.0.1:8080/solr' #solr所在服务器
#    },
#}
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_cn_backend.WhooshEngine',
        'PATH': os.path.join(os.path.dirname(__file__), 'whoosh_index'),
        },
    }
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.163.com' 
EMAIL_PORT = 25 
EMAIL_HOST_USER = '18940950618@163.com' 
EMAIL_HOST_PASSWORD = 'aizheni27564794h'
EMAIL_USE_TLS = True