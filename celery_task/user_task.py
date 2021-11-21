# -*- coding = utf-8 -*-
# @Time: 2021/11/20 17:52
# @Author: Thinkpad
# @File: user_task.py
# @Software: PyCharm
from .celery import app

@app.task
def mul(a, b):
    return a * b

