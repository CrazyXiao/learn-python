#!/usr/bin/python
# -*- coding:utf-8 -*-

# 触发任务
# 在mcelery同级目录执行 python -m mcelery.trigger

import time
from mcelery.tasks import add


result = add.delay(4, 4)
while not result.ready():
    time.sleep(1)
print ('task done: {0}'.format(result.get()))