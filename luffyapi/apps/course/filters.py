# -*- coding = utf-8 -*-
# @Time: 2021/11/20 22:54
# @Author: Thinkpad
# @File: filters.py
# @Software: PyCharm
# django-filter插件 过滤类
from django_filters.filterset import FilterSet
from . import models
from django_filters import filters
from rest_framework.filters import BaseFilterBackend

class CourseFilterSet(FilterSet):
    # 区间过滤：field_name关联的Model字段；lookup_expr设置规则；gt是大于，gte是大于等于；
    min_price = filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = filters.NumberFilter(field_name='price', lookup_expr='lte')
    class Meta:
        model = models.Course
        # 如果过滤条件仅仅就是Model已有的字段，方式一更好
        # 但是方式二可以自定义过滤字段
        fields = ['course_category', 'min_price', 'max_price']
        # fields = ['course_category']


class MyFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        min_price = request.query_params.get('min_price')
        max_price = request.query_params.get('max_price')
        if min_price and max_price:
            queryset = queryset.filter(price__gte=min_price, price__lte=max_price)
        return queryset
