# -*- coding = utf-8 -*-
# @Time: 2021/11/1 23:24
# @Author: Thinkpad
# @File: exceptions.py
# @Software: PyCharm
from rest_framework import status
from rest_framework.views import exception_handler
from .response import APIResponse
from .logger import get_logger

# logger = get_logger('django')
logger = get_logger()


def custom_exception_handler(exc, context):
    # 只要出错，就会走到这个函数，如果有值，就是捕获到了
    # 如果没有值，也是出错了，但是错误没有捕获到
    response = exception_handler(exc, context)
    print(response)
    # if response:
    # res = APIResponse(code=999, msg=response.data)
    if not response:
            # 出了异常
        res = APIResponse(code=999, msg='系统错误')
        logger.error('服务端错误，错误原因是：%s，出错的view是：%s，请求地址是：%s' % (
            str(exc),
            str(context['view']),
            context['request'].get_full_path()
        )
                     )

        return res
    return response


# def custom_exception_handler(exc, context):
#     """
#     自定义异常函数
#     exc: 异常实例对象，发生异常时实例化出来的
#     context: 字典，异常发生时python解释器收集的执行上下文信息。
#              所谓的执行上下文就是python解释器在执行代码时保存在内存中的变量、函数、类、对象、模块等一系列的信息组成的环境信息。
#     """
#     response = exception_handler(exc, context)
#     print(f"context={context}")
#     if response is None:
#         """当前异常，drf无法处理"""
#         view = context["view"] # 获取异常发生时的视图类
#         request = context["request"] # 获取异常发生时的客户端请求对象
#         if isinstance(exc, ZeroDivisionError):
#             response = APIResponse({"detail":"数学老师还有30秒达到战场，0不能作为除数！"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#
#         if isinstance(exc, TypeError):
#             print('[%s]: %s' % (view, exc))
#             response = APIResponse({'detail': '服务器内部错误'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#
#     return response