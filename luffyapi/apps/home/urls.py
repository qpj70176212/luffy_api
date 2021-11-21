# -*- coding = utf-8 -*-
# @Time: 2021/11/7 14:13
# @Author: Thinkpad
# @File: urls.py
# @Software: PyCharm
from luffyapi.apps import user
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.static import serve
from django.conf import settings

from luffyapi.apps.user import views, urls
from luffyapi.apps import user
from luffyapi.apps.home import views as home_view

# 自动生成路由
from rest_framework.routers import SimpleRouter
router = SimpleRouter()
router.register('banner', home_view.BannerView, basename='banner')
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', include(router.urls)),
    # path('', views.index),
    # path('', home_view.test_logger),
    # path('test/', home_view.TestView.as_view()),
    # re_path('^media/(?P<path>.*)', serve, {'document_root': settings.MEDIA_ROOT})
]
# urlpatterns += router.urls