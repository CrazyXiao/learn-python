#!/usr/bin/python
# -*- coding:utf-8 -*-

######################################
#   worker
#
######################################

from celery import Celery
app = Celery('mcelery', include=['mcelery.tasks'])
app.config_from_object('mcelery.config')

if __name__ == '__main__':
    app.start()