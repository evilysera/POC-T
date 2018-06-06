#!/usr/bin/env python
# -*- coding: utf-8 -*-
# project = https://github.com/Xyntax/POC-T
# author = yea@init1.in
import requests

headers = {'user-agent': 'my-app/0.0.1',
'Cookie': '',
'Origin': 'http://a.com',
}

def poc(url):
    allow_origin = ''
    if 'http://' not in url:
        url = 'http://' + url.strip()
    try:
        rsp =  requests.get(url, headers=headers,timeout=2)
        allow_origin = rsp.headers['Access-Control-Allow-Origin']
    except  requests.exceptions.ConnectionError:
        return False
    except Exception, err:
        pass
    if 'http://a.com' in allow_origin:
        return url
    else:
        return False