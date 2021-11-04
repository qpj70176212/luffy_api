# -*- coding = utf-8 -*-
# @Time: 2021/11/1 23:24
# @Author: Thinkpad
# @File: exceptions.py
# @Software: PyCharm
from rest_framework.views import exception_handler as drf_exception_handler
from .response import APIResponse
from .logger import get_logger

logger = get_logger('django')


def custom_exception_handler(exc, context):
    response = drf_exception_handler(exc, context)
    print(exc)
    print(context)
    if not response:
        # 出了异常
        res = APIResponse(code=999, msg='系统错误')
        logger.error('服务端错误，错误原因是：%s，出错的view是：%s，请求地址是：%s' % (
            str(exc), str(context['view']), context['request'].get_full_path()))
        return res
    return response
