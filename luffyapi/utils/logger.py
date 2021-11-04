# -*- coding = utf-8 -*-
# @Time: 2021/11/1 22:11
# @Author: Thinkpad
# @File: logger.py
# @Software: PyCharm
import logging

def get_logger(name):
    my_logger = logging.getLogger(name)
    return my_logger