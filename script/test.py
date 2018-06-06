#!/usr/bin/env python
# -*- coding: utf-8 -*-
# project = https://github.com/Xyntax/POC-T
# author = i@cdxy.me

"""
测试用例123
"""

import random
import time
import os
import re
from plugin.cloudeye import CloudEye


def poc(url):
    if '://' not in url:
        target = 'https://%s' % url if ':443' in url else 'http://%s' % url
    else:
        target = url
    try:
        cloudeye = CloudEye()
        # mldlkkvxjo.shiro.06pec0.ceye.io
        domain = cloudeye.getRandomDomain('shiro')  # 设置dns特征域名组
        # ping -n 3 mldlkkvxjo.shiro.06pec0.ceye.io || ping -c 3 mldlkkvxjo.shiro.06pec0.ceye.io
        rce_command = 'ping -c 2 %s' % (domain)  # 目标机执行的代码
        os.popen(rce_command)
        dnslog = cloudeye.getDnsRecord(delay=2)
        print dnslog
        if domain in dnslog:
        	msg = url
        	for remote_addr in re.findall(r'\d+\.\d+\.\d+\.\d+', dnslog):  # 获取出口ip
        		msg += ' - ' + remote_addr
        	return msg

        # remote_addr = ''
        # if domain in dnslog:
        #     msg = url
        #     data = dnslog['data']
        #     for remote_addr in data:
        #     	remote_addr = remote_addr + data['remote_addr'] + ' '
        #     msg += ' - ' + remote_addr
        #     print msg	

    except Exception, e:
        print e
    return False