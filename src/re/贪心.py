# -*- coding: utf-8 -*-
'''
Created on 2017年3月17日
@author: guanglin
'''
import re
data='Thu Feb 15 17:46:05 2017::abc@sina.com::400-123-456'

patt='\d+-\d+-\d+'
print re.search(patt, data).group()

patt='.+\d+-\d+-\d+'
print re.match(patt, data).group()

patt='.+(\d+-\d+-\d+)'
print re.match(patt, data).group(1)

patt='.+?(\d+-\d+-\d+)'
print re.match(patt, data).group(1)