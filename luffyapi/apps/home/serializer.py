# -*- coding = utf-8 -*-
# @Time: 2021/11/2 23:08
# @Author: Thinkpad
# @File: serializer.py
# @Software: PyCharm
from rest_framework import serializers
from .models import Banner
class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = ['id', 'link', 'image']

    image = serializers.SerializerMethodField()
    def get_image(self, obj):
        print( obj.image)

        return  'http://127.0.0.1:8000/media/' + str(obj.image)  # 把对象转成字符串