# -*- coding: utf-8 -*-
'''
Created on 2017年4月5日
@author: guanglin
'''
import urllib,urllib2
log_val={}
log_val['username']='liugl@ydynasty.com'
log_val['passwd']='123456'
data=urllib.urlencode(log_val)
url='http://kj.ydynasty.com/app/index.html#/user/login'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent } 
req=urllib2.Request(url,data,headers)
req.get_method=lambda:'HEAD'
webpage=urllib2.urlopen(req)
print webpage.getcode()
print webpage.info()
print webpage.read()

# get_val={}
# get_val['mobile']='13800138000'
# get_val['action']='mobile'
# data=urllib.urlencode(get_val)
# url='http://www.ip138.com:8080/search.asp'
# geturl=url+'?'+data
# req=urllib2.Request(geturl)
# resp=urllib2.urlopen(req)
# print resp.info()