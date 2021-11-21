# -*- coding = utf-8 -*-
# @Time: 2021/11/6 17:11
# @Author: Thinkpad
# @File: serializer.py
# @Software: PyCharm
import re
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.settings import api_settings
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
from django.core.cache import cache
from luffyapi.apps.user import models
from django.conf import settings


class UserModelSerializer(serializers.ModelSerializer):
    # 必须重写一下username字段
    username = serializers.CharField()

    class Meta:
        model = models.User
        fields = ['username', 'password']
        extra_kwargs = {
            'username': {'write_only': True},
            'password': {'write_only': True},
        }

    # 全局钩子（校验用户名密码是否正确，登录成功，签发token）
    def validate(self, attrs):
        # 取出用户名密码
        username = attrs.get('username')
        password = attrs.get('password')
        # 手机号
        if re.match('^1[3-9][0-9]{9}$', username):
            user = models.User.objects.filter(mobile=username).first()
        # 邮箱
        elif re.match('^.+@.+$', username):
            user = models.User.objects.filter(email=username).first()
        # 用户名
        else:
            user = models.User.objects.filter(username=username).first()
        # 校验user，校验密码
        if user and user.check_password(password):
            # 签发token
            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)
            self.context['token'] = token
            # self.context['username'] = user.username
            # self.context['id'] = user.id
            # 将登录用户对象直接传给视图
            self.context['user'] = user
            # 通过请求头格式化icon
            # request = self.context['request']
            return attrs
        else:
            raise ValidationError('用户名或密码错误！')

    # def UserModelSerializer(self, user):
    #     pass


class UserPhoneModelSerializer(serializers.ModelSerializer):
    # 必须重写一下code字段
    code = serializers.CharField()
    mobile = serializers.CharField(max_length=11)
    class Meta:
        model = models.User
        fields = ['mobile', 'code']

    # 全局钩子（校验手机号和验证码是否正确，登录成功，签发token）
    def validate(self, attrs):
        # 取出用户名密码
        mobile = attrs.get('mobile')
        code = attrs.get('code')
        # 从缓存中取出这个手机号对应的验证码
        cache_code = cache.get(settings.SMS_CACHE_PHONE % mobile)
        if cache_code and cache_code == code:
            # 可以登录，根据手机号，查到用户，给这个用户签发token
            user = models.User.objects.get(mobile=mobile)
            # 签发token
            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)
            self.context['token'] = token
            # 将登录用户对象直接传给视图
            self.context['user'] = user
            return attrs
        else:
            raise ValidationError("验证码错误")


class UserRegisterModelSerializer(serializers.ModelSerializer):
    # 必须重写一下code字段
    code = serializers.CharField(write_only=True)

    class Meta:
        model = models.User
        fields = ['mobile', 'code', 'password']

        # code这个字段只用来写
        # extra_kwargs = {
        #     'code': {'write_only': True}
        # }

    # 可以给手机号和password加局部校验钩子
    def validate_mobile(self, data):
        # 手机号
        if re.match('^1[3-9][0-9]{9}$', data):
           return data
        else:
            raise ValidationError("手机号不合法！")


    # 全局钩子
    def validate(self, attrs):
        # 取出用户名密码
        mobile = attrs.get('mobile')
        code = attrs.get('code')
        # 从缓存中取出这个手机号对应的验证码
        cache_code = cache.get(settings.SMS_CACHE_PHONE % mobile)
        if cache_code and cache_code == code:
            # 可以注册
            # 如何注册？ 需要重写create，由于密码是密文，需要重写，使用create_user来创建用户
            # 把code剔除
            attrs.pop('code')
            # 加入username
            attrs['username'] = mobile

            return attrs
        else:
            raise ValidationError("验证码错误")

    def create(self, validated_data):
        # validated_data: username,password,mobile (email,icon都可以为空)
        user = models.User.objects.create_user(**validated_data)
        return user
