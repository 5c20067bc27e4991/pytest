# -*- coding: utf-8 -*-
'''
Created on 2017年3月20日
@author: guanglin
'''
import requests
import urllib.request, urllib.parse, urllib.error
import urllib.request, urllib.error, urllib.parse

page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
try:
    request = urllib.request.Request(url,headers = headers)
    response = urllib.request.urlopen(request)
    print(response.read())
except urllib.error.URLError as e:
    if hasattr(e,"code"):
        print(e.code)
    if hasattr(e,"reason"):
        print(e.reason)