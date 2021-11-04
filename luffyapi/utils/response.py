# -*- coding = utf-8 -*-
# @Time: 2021/11/1 22:48
# @Author: Thinkpad
# @File: response.py
# @Software: PyCharm
from rest_framework.response import Response


class APIResponse(Response):
    def __init__(self, code=100, msg='成功', data=None, status=None,
                 headers=None, exception=False, content_type=None, **kwargs):
        real_data = {
            'code': code,
            'msg': msg,
            'data': data
        }
        if kwargs:
            data.update(kwargs)
        super().__init__(data=real_data, status=status, headers=headers, exception=exception, content_type=content_type)
