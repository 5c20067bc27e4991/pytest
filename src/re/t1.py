# -*- coding: utf-8 -*-
'''
Created on 2017年3月17日
@author: guanglin
'''
import re, time

s = 'abc123efg456'
p = '[a-z]+(\d+).*'
t1 = time.time()
rec = re.compile(p)
for i in range(10000):
    #     print rec.match(s).groups()
    re.match(p, s).group(1)
t2 = time.time()
print(t2 - t1)