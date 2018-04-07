#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import urllib
import urllib2

baseurl = 'http://www.baidu.com/'
UA = {
    'User-Agent': 'User-Agent:Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.888'}

keys = raw_input('Search key: ')
wd = {'wd': keys}
wd = urllib.urlencode(wd)
search_url = 's?'+ wd
request = urllib2.Request(baseurl + search_url, headers=UA)
request.add_header('header1', 'hehe')
reponse = urllib2.urlopen(request)
print(request.get_full_url())

#get_header()参数首字母必须大写，剩余均小写
print(request.get_header('User-Agent'))
print(request.get_header('Header1'))
print(reponse.code)
html = reponse.read()
with open('baidu.html','w') as f:
    f.write(html)

print('Done!')
