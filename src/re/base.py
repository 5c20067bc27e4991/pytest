# -*- coding: utf-8 -*-
'''
Created on 2017年3月14日
@author: guanglin
'''
import re
# m = re.match(r'(\w+) (\w+)(?P<sign>.*)', 'hello world!')
str1='abc-123'
pt1='(\w\w(\w))-(\d\d\d)'
m=re.match(pt1, str1)
s=re.search(pt1, str1)
if m is None:
    print('m is None.')
else:
    print('m.group()=> ',m.group(1))
    print('m.groups()=> ',m.groups())
if s is None:
    print('m is None.')
else:
    print('s.group()=> ',s.group())
    print('s.groups()=> ',s.groups())
    
print('re.findall==> ',re.findall('(\w\w(\w))-(\d\d\d)','abc-123'))

print(re.sub('-+','SB','Hello -. Hi --.'))
print(re.subn('X','SB','Hello X. Hi X.'))
print(re.split('[\s]+','str1 str2     str3 str4' ,2))