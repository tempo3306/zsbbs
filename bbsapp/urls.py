# encoding: utf-8
'''
@author: zhushen
@contact: 810909753@q.com
@time: 2017/12/9 20:12
'''
from django.conf.urls import url,include
from bbsapp import views as bbsapp_view

urlpatterns = [
    url(r'^$',bbsapp_view.index,name='HOME'),
    url(r'^create_post/$',bbsapp_view.create_post,name='create_post'),
    url(r'^tinymce/', include('tinymce.urls')),
]