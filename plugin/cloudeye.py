#!/usr/bin/env python
# -*- coding: utf-8 -*-
# project = https://github.com/Xyntax/POC-T
# author = i@cdxy.me


"""
CloudEye API

Usage:
    c = CloudEye()
    a = c.getRandomDomain('cdxy')
    try:
        requests.get('http://' + a, timeout=1)
    except Exception:
        pass
    print c.verifyDNS(delay=0)
    print c.verifyHTTP(delay=0)
    print c.getDnsRecord(delay=0)
    print c.getHttpRecord(delay=0)
"""

import random
import requests
import time
from string import ascii_lowercase
from lib.utils.config import ConfigFileParser

# load once for all thread
key = ConfigFileParser().CloudEyeApikey()
uniq_domain = ConfigFileParser().ColudEyePersonaldomain().split('.')[0]


class CloudEye:
    def __init__(self):
        self.unique = uniq_domain
        self.random = ''.join([random.choice(ascii_lowercase) for _ in range(10)])

    def getRandomDomain(self, custom='poc'):
        """
        full domain = [random].[custom].[unique].dnslog.info
        mldlkkvxjo.shiro.06pec0.ceye.io
        """
        self.custom = custom
        return '%s.%s.%s.ceye.io' % (self.random, self.custom, self.unique)

    def getDnsRecord(self, delay=2):
        time.sleep(delay)
        query = self.random + '.' + self.custom
        api_base = 'http://api.ceye.io/v1/records?token={key}&type=dns&filter={domain}'.format(key=key, domain=query)
        return requests.get(api_base).content

    def getHttpRecord(self, delay=2):
        time.sleep(delay)
        query = self.random + '.' + self.custom
        api_base = 'http://api.ceye.io/v1/records?token={key}&type=request&filter={domain}'.format(key=key, domain=query)
        return requests.get(api_base).content

    def verifyDNS(self, delay=2):
        return 'dnslog.info' in self.getDnsRecord(delay)

    def verifyHTTP(self, delay=2):
        return 'dnslog.info' in self.getHttpRecord(delay)


def queryDnsRecord(domain, delay=2):
    time.sleep(delay)
    domain = domain.replace(uniq_domain + '.dnslog.info', '').rstrip('.')
    api_base = 'http://api.ceye.io/v1/records?token={key}&type=dns&filter={domain}'.format(key=key, domain=query)
    return requests.get(api_base).content


def queryHttpRecord(domain, delay=2):
    time.sleep(delay)
    domain = domain.replace(uniq_domain + '.dnslog.info', '').rstrip('.')
    api_base = 'http://api.ceye.io/v1/records?token={key}&type=request&filter={domain}'.format(key=key, domain=query)
    return requests.get(api_base).content
