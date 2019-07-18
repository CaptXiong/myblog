from django.conf.urls import include,url
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

app_name = 'post'   # 这里是为了url反向解析用

urlpatterns = [
    path('', views.index,name='index'),
    path('blog/',views.blog,name='blog'),
    # url(r'^detail/post-(?P<pk>\d+)$', views.detail, name="detail"),
    path('detail-<pk>', views.detail, name="detail")
]
