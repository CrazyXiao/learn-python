#!/usr/bin/python
# -*- coding:utf-8 -*-

#####################################
# 配置celery的broker backend
#
######################################
from datetime import timedelta
from celery.schedules import crontab

CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/5'
BROKER_URL = 'redis://127.0.0.1:6379/6'

# 定时
CELERY_TIMEZONE = 'Asia/Shanghai'
CELERYBEAT_SCHEDULE = {
    'add-every-30-seconds': {
         'task': 'mcelery.tasks.add',
         'schedule': timedelta(seconds=5),
         'args': (16, 16)
    },
    # Executes every Monday morning at 7:30 A.M
    'add-every-monday-morning': {
        'task': 'mcelery.tasks.add',
        'schedule': crontab(hour=7, minute=30, day_of_week=1),
        'args': (5, 5),
    },
}
