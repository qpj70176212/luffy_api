import re
from django.shortcuts import render, HttpResponse
from luffyapi.utils.response import APIResponse
from luffyapi.apps.user import models
from rest_framework.viewsets import ViewSet, ViewSetMixin
from .serializer import UserModelSerializer, UserPhoneModelSerializer, UserRegisterModelSerializer
from rest_framework.decorators import action
from luffyapi.libs.tx_sms import get_code, send
from django.core.cache import cache
from django.conf import settings
from .throttlings import SMSThrottle
from rest_framework.views import APIView
# Create your views here.

def index(request):
    print(request.method)  # OPTIONS
    res = HttpResponse('hello world')
    # res['Access-Control-Allow-Origin'] = 'http://192.168.19.244:8080'
    # res['Access-Control-Allow-Origin'] = '*'

    # if request.method == 'OPTIONS':
    #     res['Access-Control-Allow-Methods'] = '*'
    #     res['Access-Control-Allow-Origin'] = '*'
    #     res['Access-Control-Allow-Headers'] = '*'
    return res


# 登录接口
# 自动生成路由，post请求，跟数据有关系

# class LoginView(ViewSetMixin, APIView):
class UserView(ViewSet):
    @action(methods=['POST'], detail=False)
    def login(self, request, *args, **kwargs):
        # 序列化类
        ser = UserModelSerializer(data=request.data)
        if ser.is_valid():
            # 登录成功
            token = ser.context['token']
            user = ser.context['user']
            # id = ser.context['id']
            # print(id)
            # print(ser.data)
            # print(ser.data.get('id'))
            # ser.instance.id 取不到

            # user = ser.context.get('user')
            # result = ser.UserModelSerializer(user).data
            return APIResponse(token=token, username=user.username, id=user.id)
            # result['token'] = token  # id，username，icon，token
            # return APIResponse(result=result)
        else:
            # 登录失败
            # return APIResponse(code=101, msg=ser.errors)
            return APIResponse(code=101, msg='用户名或密码错误')

    @action(methods=['POST'], detail=False)
    def login_phone(self, request, *args, **kwargs):
        # 序列化类 手机号+验证码
        ser = UserPhoneModelSerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        token = ser.context['token']
        user = ser.context['user']
        return APIResponse(token=token, username=user.username, id=user.id)

    @action(methods=['POST'], detail=False)
    def register(self, request, *args, **kwargs):
        # 序列化类
        ser = UserRegisterModelSerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        ser.save()  # 新增会触发，serializer的create方法
        return APIResponse(code=100, msg="注册成功")

    # @action(methods=['POST'], detail=False, throttle_classes=[类名])
    # def send_sms(self, request, *args, **kwargs):

    # 手机号是否存在接口  get: user/check_phone?phone=1333333
    # 自动生成路由，把它直接写到原来写login的视图类中
    @action(methods=['GET'], detail=False)
    def check_phone(self, request, *args, **kwargs):
        phone = request.query_params.get('phone')
        if re.match('^1[3-9][0-9]{9}$', phone):
            user = models.User.objects.filter(mobile=phone).first()
            if user:
                return APIResponse(msg='手机号存在')
            else:
                return APIResponse(code=101, msg='手机号不存在')
        else:
            return APIResponse(code=102, msg='手机号不合法')


class SmsView(ViewSet):
    throttle_classes = [SMSThrottle]

    # 发送短信接口  http://127.0.0.1:8000/user/send_sms/?phone=17260808696
    # 限制同一个手机号短信一分钟，只能发一次
    @action(methods=["GET"], detail=False)
    # @throttle_classes(类名)
    def send_sms(self, request, *args, **kwargs):
        phone = request.query_params.get('phone')
        if phone:
            if re.match('^1[3-9][0-9]{9}$', phone):
                code = get_code()
                res = send(phone, code)
                # print(phone, type(phone))
                # 短信验证码，存在哪？ django缓存中（默认在内存中，redis）
                # 设置：cache.set(键,值,有效时间)
                cache.set(settings.SMS_CACHE_PHONE % phone, code, 60)
                # cache.set("sms_cache_phone_%s" % (phone,), code, 60)
                # print(settings.SMS_CACHE_PHONE)  # sms_cache_phone_%s
                if res:
                    return APIResponse(msg='短信发送成功')
                else:
                    return APIResponse(code=101, msg='短信发送失败')
            else:
                return APIResponse(code=102, msg='手机号不合法')

        else:
            return APIResponse(code=103, msg='没有携带手机号')

from luffyapi.libs.redis_pool import POOL
from redis import Redis
# def test(request):
#     conn = Redis(connection_pool=POOL)
#     name = conn.get('name')
#     return HttpResponse('name是: %s' % name)

from django_redis import get_redis_connection

def test(request):
    # 从连接池中取一个连接
    conn = get_redis_connection()
    name = conn.get('name')
    return HttpResponse('name的value是: %s' % name)