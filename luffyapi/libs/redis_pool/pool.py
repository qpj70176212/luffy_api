# -*- coding = utf-8 -*-
# @Time: 2021/11/19 23:42
# @Author: Thinkpad
# @File: pool.py
# @Software: PyCharm
from redis import ConnectionPool
POOL = ConnectionPool(max_connections=5, host='127.0.0.1', port=6379)
