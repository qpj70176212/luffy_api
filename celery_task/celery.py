# -*- coding = utf-8 -*-
# @Time: 2021/11/20 17:53
# @Author: Thinkpad
# @File: celery.py
# @Software: PyCharm
# 从脚本中导入django环境
import django
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'luffyapi.settings.dev')
django.setup()

backend = 'redis://127.0.0.1:6379/1'
# 消息中间件
broker = 'redis://127.0.0.1:6379/2'
app = Celery(main=__name__, backend=backend, broker=broker,
             include=['celery_task.course_task', 'celery_task.user_task', 'luffyapi.apps.home.home_task'])

# 修改时区
# 时区
app.conf.timezone = 'Asia/Shanghai'
# 是否使用UTC
app.conf.enable_utc = False

# 执行定时任务（通过配置，配置beat，识别我们的配置，定时提交任务）
# 启动beat，启动worker

# 任务定时配置
from datetime import timedelta
from celery.schedules import crontab
app.conf.beat_schedule = {
    'update_banner': {
        'task': 'luffyapi.apps.home_task.update_banner',
        'schedule': timedelta(seconds=3),  # 3s后
    }
}

# 启动beat
# celery -A celery_task beat -l info