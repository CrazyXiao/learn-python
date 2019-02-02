#! /usr/bin/python
# -*- coding: utf-8 -*-

############################################
#
#  日志模块
#
############################################
import os
import sys
import logging

DEFAULT_LOG_NAME = 'access.log'

def logger_init(name=None, level=logging.DEBUG):
    if not name:
        name = DEFAULT_LOG_NAME
    filepath = os.path.join(os.path.dirname(__file__), os.pardir, 'log', name)
    logger = logging.getLogger()
    logger.setLevel(level)
    ch = logging.FileHandler(filepath)
    formatter = logging.Formatter('[%(asctime)s] [%(filename)s:%(lineno)d] [%(levelname)s] %(message)s',
                                  datefmt='%Y-%m-%d %H:%M:%S')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger

def simple_log_init(level=logging.DEBUG):
    log_format = '[%(asctime)s] [%(filename)s:%(lineno)d] [%(levelname)s] %(message)s'
    logging.basicConfig(stream=sys.stdout, level=level, format=log_format)
    return logging

logger = logger_init()

if __name__ == '__main__':
    logger = logger_init('hello.log')
    logger.debug('hello world')