# POC-T: *Pentest Over Concurrent Toolkit* 
[![Python 2.7](https://img.shields.io/badge/python-2.7-yellow.svg)](https://www.python.org/) [![License](https://img.shields.io/badge/license-GPLv2-red.svg)](https://raw.githubusercontent.com/Xyntax/POC-T/master/doc/LICENSE.txt) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/1413552d34bc4a4aa84539db1780eb56)](https://www.codacy.com/app/xyntax/POC-T?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Xyntax/POC-T&amp;utm_campaign=Badge_Grade) [![PoC/Scripts](https://img.shields.io/badge/PoC/Scripts-52-blue.svg)](https://github.com/Xyntax/POC-T/wiki/%E5%86%85%E7%BD%AE%E8%84%9A%E6%9C%AC%E5%BA%93) 

脚本调用框架，用于渗透测试中 **采集|爬虫|爆破|批量PoC** 等需要并发的任务。  


特点
---
* 支持多线程/Gevent两种并发模式  
* 极简式脚本编写，无需参考文档  
* 内置脚本扩展及常用PoC函数  
* 支持第三方搜索引擎API(已完成ZoomEye/Shodan/Google/Fofa免费版)  



更新
----
- 修改cloudeye接口，对接[ceye](http://ceye.io)
- 新增存活扫描：alive_domain.py
- 修改shiro反序列化扫描：shiro-deserial-rce.py
- 新增cors扫描：cors.py
- 修改weblogic wls xmldecode反序列化：weblogic-wls.py


Tips
----
- script 自动补全
	- 添加alias
		```shell
		alias poc-cd="cd /Users/yea/tool/git/POC-T/script/"
		alias poc-t="python /Users/yea/tool/git/POC-T/POC-T.py"
		```
	- poc-t -s shiro-deserial-rce.py -iS a.com

联系作者
----
* mail:yea@init1.in

  
