#! /usr/bin/python
# -*- coding: utf-8 -*-

########################################
#
#    公共模块
#
########################################
import os
import yaml
import redis


# 项目目录
PROJECT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))

# 获取配置文件信息
with open(os.path.join(PROJECT_DIR, 'config', 'config.yaml')) as fd:
    config = yaml.load(fd)

redis_client = redis.Redis(host=config['redis']['host'],
                           port=config['redis']['port'],
                           db=config['redis']['db'],
                           password=config['redis']['password']
                           )

pool = None
def get_redis_db():
    global pool
    if not pool:
        pool = redis.ConnectionPool(host=config['redis']['host'],
                                                    port=config['redis']['port'],
                                                    db=config['redis']['db'],
                                                    password=config['redis']['password'])
    return redis.Redis(connection_pool=pool)
redisdb = get_redis_db()


