# -*- coding = utf-8 -*-
# @Time: 2021/11/20 18:23
# @Author: Thinkpad
# @File: home_task.py
# @Software: PyCharm
from celery_task import app
from home.models import Banner
from home.serializer import BannerSerializer
from django.conf import settings
# @app.task
# def add(a, b):
#     import time
#     time.sleep(10)
#     return a + b

@app.task
def update_banner():
    from home.models import Banner
    from home.serializer import BannerSerializer
    from django.conf import settings
    from django.core.cache import cache
    # 更新轮播图缓存的任务
    # 只要这个task被执行一次，缓存中的轮播图就是最新的

    queryset = Banner.objects.all().filter(is_show=True, is_delete=False).order_by('-orders')[0:settings.BANNER_SIZE]
    ser = BannerSerializer(instance=queryset, many=True)
    # 小问题，图片前面的路径是没有带的，处理路径
    for item in ser.data:
        item['image'] = settings.REMOTE_ADDR + item['image']

    cache.set('banner_cache_list', ser.data)
    return True