from django.shortcuts import render
# Create your views here.
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from . import models, serializers


# 课程分类群查
class CourseCategoryViewSet(GenericViewSet, ListModelMixin):
    queryset = models.CourseCategory.objects.filter(is_delete=False, is_show=True).all()
    serializer_class = serializers.CourseCategorySerializer

# 课程群查

# 分页组件：基础分页(采用)、偏移分页、游标分页(了解)
from . import pagination

# 过滤组件：搜索功能、排序功能
from rest_framework.filters import SearchFilter, OrderingFilter

# django-filter插件：分类功能
from django_filters.rest_framework import DjangoFilterBackend
from .filters import CourseFilterSet
# from .filters import MyFilter

# 前台携带所有过滤规则的请求url：
# http://127.0.0.1:8000/course/free/?page=1&page_size=10&search=python&ordering=-price&min_price=30&count=1


class CourseViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    queryset = models.Course.objects.filter(is_delete=False, is_show=True).all()
    serializer_class = serializers.CourseSerializer

    # 分页组件
    pagination_class = pagination.PageNumberPagination

    # 过滤组件：实际开发，有多个过滤条件时，要把优先级高的放在前面
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    # filter_backends = [MyFilter]

    # 参与搜索的字段
    search_fields = ['name', 'id', 'brief']

    # 允许排序的字段
    ordering_fields = ['id', 'price', 'students']

    # 过滤类：分类过滤、区间过滤
    filter_class = CourseFilterSet
    # filter_fields = ('course_category',)


# 一个课程的所有章节（群查）
class ChapterViewSet(GenericViewSet, ListModelMixin):
    queryset = models.CourseChapter.objects.filter(is_delete=False, is_show=True).all()
    serializer_class = serializers.CourseChapterSerializer

    # 基于课程分类条件下的查询
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['course']


# 搜索课程接口
class SearchCourseViewSet(GenericViewSet, ListModelMixin):
    queryset = models.Course.objects.filter(is_delete=False, is_show=True).all()
    serializer_class = serializers.CourseSerializer

    pagination_class = pagination.PageNumberPagination

    filter_backends = [SearchFilter]
    search_fields = ['name']