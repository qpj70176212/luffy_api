# -*- coding = utf-8 -*-
# @Time: 2021/11/13 18:41
# @Author: Thinkpad
# @File: send_sms.py
# @Software: PyCharm
import random
from qcloudsms_py import SmsSingleSender

from . import settings
from luffyapi.utils.logger import get_logger

logger = get_logger()


# 随机生成四位数字验证码
# 字符串+数字 在python中报错 ---> python是动态强类型（不同类型之间不能运算）
def get_code():
    code = ""
    for i in range(6):
        code += str(random.randint(0, 9))
    return code



def send(phone, code):
    ssender = SmsSingleSender(settings.APPID, settings.APPKEY)
    try:
        result = ssender.send_with_param(86, phone,
                                         settings.TEMPLATE_ID, [code, 5], sign=settings.SMS_SIGN, extend="", ext="")
        # print(result)  # 字典 {'result': 0, 'errmsg': 'OK', 'ext': '', 'sid': '2109:237813562916368170055530869', 'fee': 1, 'isocode': 'CN'}
        if result.get("result") == 0:
            return True
        else:
            # 记录日志
            logger.warning(msg="$s手机号，短信发送失败" % phone)
            return False
    except Exception as e:
        # 记录日志
        logger.warning(msg="$s手机号，短信发送时出现异常" % phone)
        return False



