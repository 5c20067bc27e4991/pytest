#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib
import urllib2

url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
headers = {"Accept": "application/json, text/javascript, */*; q=0.01",
           # "Accept-Encoding": "gzip, deflate",
           "Accept-Language": "zh-CN,zh;q=0.8",
           "Cache-Control": "no-cache",
           "Connection": "keep-alive",
           "Content-Length": "218",
           "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
           "Cookie": "_ntes_nnid=2e94214f39d098becea7e719f29e7388,1503509728979; OUTFOX_SEARCH_USER_ID_NCOO=137259988.93608335; OUTFOX_SEARCH_USER_ID=85118875@114.240.120.208; _ga=GA1.2.1123654366.1505835504; DICT_UGC=be3af0da19b5c5e6aa4e17bd8d90b28a|; JSESSIONID=abcb-RAFeVNK8hfjNqukw; ___rl__test__cookies=1522906820807",
           "Host": "fanyi.youdao.com",
           # "Origin:http": "//fanyi.youdao.com",
           "Pragma": "no-cache",
           # "Referer:http": "//fanyi.youdao.com/",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
           "X-Requested-With": "XMLHttpRequest"}

# key = raw_input('Input:')
formdata = {"i": "你好",
            "from": "AUTO",
            "to": "AUTO",
            "smartresult": "dict",
            "client": "fanyideskweb",
            "salt": "1522906820817",
            "sign": "3046ed2fcd0b90ba5c6a59aca7396a25",
            "doctype": "json",
            "version": "2.1",
            "keyfrom": "fanyi.web",
            "action": "FY_BY_CLICKBUTTION",
            "typoResult": "false"}

data = urllib.urlencode(formdata)

req = urllib2.Request(url, data=data, headers=headers)
print(urllib2.urlopen(req).read())
