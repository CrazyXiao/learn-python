#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

import sys
import subprocess
import traceback
class CalledCommandError(Exception):
    def __init__(self, returncode, cmd, errorlog,output):
        self.returncode = returncode
        self.cmd = cmd
        self.output = output
        self.errorlog = errorlog
    def __str__(self):
        return "命令运行错误:'%s',返回值: %s,错误信息： %s" % (self.cmd, str(self.returncode) ,self.errorlog)
def runCommand(*popenargs, **kwargs):
    cmd = popenargs[0]
    allresult = {}

    if 'stdout' in kwargs or 'stderr' in kwargs :
        raise ValueError('标准输出和标准错误输出已经定义，不需设置。')
    process = subprocess.Popen(stdout=subprocess.PIPE,shell=True,stderr = subprocess.PIPE,*popenargs, **kwargs)
    output, unused_err = process.communicate()
    returncode = process.poll()
    allresult['success'] = True
    allresult['errorlog'] = unused_err
    if returncode !=0:
        allresult['success'] = False
    if returncode ==124 :
        allresult['errorlog'] = "异常通信"

    allresult['returncode'] = returncode
    allresult['cmd'] = cmd
    allresult['outdata'] = output
    return allresult


if __name__ == '__main__':
    """"
        当独执行此文件，先设置环境变量
        export PYTHONPATH=/Data/python/
        @param: </usr/bin/ssh root@172.16.5.96 "bash -s"  < /home/py/shell/shutdown.sh>
        """
    cmd = sys.argv[1]
    try:
        e=runCommand(cmd)
        print (e)
    except Exception as re:
        print(re)
        traceback.print_exc()