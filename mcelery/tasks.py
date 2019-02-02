#!/usr/bin/python
# -*- coding:utf-8 -*-

###################################
#   任务
#
####################################
from mcelery.celery import app

@app.task
def add(x, y):
    return x + y