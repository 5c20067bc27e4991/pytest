# -*- coding: utf-8 -*-
'''
Created on 2017年3月13日
@author: guanglin
'''
from functools import reduce

print(list(filter((lambda x:x%2),list(range(9)))))
print(list(map((lambda x:x+2),list(range(5)))))
print(list(map(lambda x,y:x+y ,[1,3,5],[2,4,6])))
print(reduce((lambda x,y:x+y), list(range(5))))