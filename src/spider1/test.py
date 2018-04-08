#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import requests

r=requests.get('http://www.baidu.com')
print(r.content.decode())
print(r.text)
print(r.url)
