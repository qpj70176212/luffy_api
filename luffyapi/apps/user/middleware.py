# -*- coding = utf-8 -*-
# @Time: 2021/11/1 14:27
# @Author: Thinkpad
# @File: middleware.py
# @Software: PyCharm
from django.utils.deprecation import MiddlewareMixin
class CORSMiddleWare(MiddlewareMixin):
    def process_response(self, request, response):
        if request.method == 'OPTIONS':
            response['Access-Control-Allow-Headers'] = '*'
            response['Access-Control-Allow-Methods'] = '*'
        response['Access-Control-Allow-Origin'] = '*'


        return response