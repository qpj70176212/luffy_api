# -*- coding = utf-8 -*-
# @Time: 2021/11/2 20:57
# @Author: Thinkpad
# @File: models.py
# @Software: PyCharm
from django.db import models

# 所有表的基类
# class BaseModel(models.Model):
#     create_time = models.DateTimeField(auto_now_add=True)
#     last_update = models.DateTimeField(auto_now=True)
#     order = models.IntegerField(help_text='顺序')
#     is_show = models.BooleanField(default=False)
#     is_delete = models.BooleanField(default=False)  # 软删除


from django.db import models

class BaseModel(models.Model):
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_time = models.DateTimeField(auto_now=True, verbose_name='最后更新时间')
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')
    is_show = models.BooleanField(default=True, verbose_name='是否上架')
    orders = models.IntegerField(verbose_name='优先级')

    class Meta:
        abstract = True  # 虚拟表，只用来继承，不再数据库生成
