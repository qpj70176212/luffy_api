# -*- coding = utf-8 -*-
# @Time: 2021/11/20 22:47
# @Author: Thinkpad
# @File: serializer.py
# @Software: PyCharm
from rest_framework import serializers
from . import models


class CourseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CourseCategory
        fields = ('id', 'name')


# 子序列化
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Teacher
        fields = ('name', 'role_name', 'title', 'signature', 'image', 'brief')


class CourseSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer(many=False)
    # course_section = serializers.SerializerMethodField()
    # def get_course_section(self):
    #     pass

    class Meta:
        model = models.Course
        fields = (
            'id',
            'name',
            'course_img',
            'brief',
            'attachment_path',
            'pub_sections',
            'price',
            'students',
            'period',
            'sections',
            'course_type_name',  #
            'level_name',  #
            'status_name',  #
            'teacher',
            'section_list',
            'course_category'
        )


# 课程课时
class CourseSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CourseSection
        fields = ('name', 'orders', 'section_link', 'duration', 'free_trail')


# 课程章节
class CourseChapterSerializer(serializers.ModelSerializer):
    # 子序列化方式实现 一个章节下有很多课时 必须many=True
    coursesections = CourseSectionSerializer(many=True)
    class Meta:
        model = models.CourseChapter
        fields = ('name', 'chapter', 'summary', 'coursesections', 'course')