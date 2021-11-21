# -*- coding = utf-8 -*-
# @Time: 2021/11/13 23:27
# @Author: Thinkpad
# @File: throttlings.py
# @Software: PyCharm
from rest_framework.throttling import SimpleRateThrottle
# 重写get_cache_key 返回谁就以谁作为key来限制

# 限制1分钟只能访问1次的频率类
class SMSThrottle(SimpleRateThrottle):
    scope = 'sms'
    def get_cache_key(self, request, view):
        phone = request.query_params.get('phone')
        #  cache_format = 'throttle_%(scope)s_%(ident)s'
        return self.cache_format % {'scope': self.scope, 'ident': phone}