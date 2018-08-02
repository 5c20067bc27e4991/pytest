# -*- coding: utf-8 -*-
'''
Created on 2017年3月24日
@author: guanglin
'''
import random, time

lst = list(range(10))
random.shuffle(lst)
# t1=time.time()    
print(lst)
for i in range(len(lst) - 1):
    for j in range(len(lst) - 1 - i):
        if lst[j] > lst[j + 1]:
            # t=lst[j]
            # lst[j]=lst[j+1]
            # lst[j+1]=t
            lst[j], lst[j + 1] = lst[j + 1], lst[j]
#     print lst
print(lst)
# t2=time.time()
# print t2-t1
