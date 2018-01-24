# -*- coding: utf-8 -*-
'''
Created on 2017年3月13日
@author: guanglin
'''

print filter((lambda x:x%2),range(9))
print map((lambda x:x+2),range(5))
print map(lambda x,y:x+y ,[1,3,5],[2,4,6])
print reduce((lambda x,y:x+y), range(5))