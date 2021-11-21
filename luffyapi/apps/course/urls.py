# -*- coding = utf-8 -*-
# @Time: 2021/11/20 22:49
# @Author: Thinkpad
# @File: urls.py
# @Software: PyCharm
from django.urls import path, re_path, include
from . import views

# 自动生成路由
from rest_framework.routers import SimpleRouter
router = SimpleRouter()

router.register('categories', views.CourseCategoryViewSet, 'categories')  # 分类
router.register('course', views.CourseViewSet, 'actualcourse')  # 课程
router.register('chapters', views.ChapterViewSet, 'chapter')  # 章节
router.register('search', views.SearchCourseViewSet, 'search')  # 搜索课程

urlpatterns = [
    path('', include(router.urls)),

]
# urlpatterns += router.urls