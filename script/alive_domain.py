#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@Author：ysera@init.in
'''
import requests
import sys
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0','Connection': 'keep-alive','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8','Accept-Encoding': 'gzip, deflate'}
    
def poc(url):
    filename =  sys.argv[4].split('.txt')[0] + '.alive.txt'
    url = url.split(' ')[0]
    if '://' not in url:
        target = 'https://%s' % url if ':443' in url else 'http://%s' % url
    else:
        target = url
    try:
        f = open(filename,'a')
        rsp = requests.get(target.strip(), headers=headers, verify=False, allow_redirects=True, timeout=10)
        f.write(url+'\n')
        return False
    except Exception, e:
        pass
    return url   
