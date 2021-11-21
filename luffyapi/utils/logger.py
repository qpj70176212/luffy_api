# -*- coding = utf-8 -*-
# @Time: 2021/11/1 22:11
# @Author: Thinkpad
# @File: logger.py
# @Software: PyCharm
import logging

# def get_logger(name):
def get_logger():
    my_logger = logging.getLogger('django')
    return my_logger