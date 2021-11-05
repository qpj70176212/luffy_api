# -*- coding = utf-8 -*-
# @Time: 2021/11/1 23:56
# @Author: Thinkpad
# @File: s1.py
# @Software: PyCharm
# 记录详细异常
import traceback

try:
    a = [1, 2, 34]
    print(a[9])
except Exception as e:
    # print(e)  # list index out of range
    res = traceback.format_exc()
    print(res)
    # logger.error(res)

    # sentry: 开源的使用django开发的无关平台的日志记录及分析的项目
print("hello world")

print('本地dev开发新功能')

# 测试本地分支合并到远程
print('本地dev开发新功能2')