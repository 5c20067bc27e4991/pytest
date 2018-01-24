# -*- coding: utf-8 -*-
'''
Created on 2017年3月18日
@author: guanglin
'''
a1=11
def mularg(a1,a2=999,*tup_arg,**dic_arg):
    print 'a1=>',a1
    print 'a2=>',a2
    for e in tup_arg:
        print e
    for k in dic_arg.keys():
        print '%s-->%s' %(k,dic_arg[k])
        
mularg(1,888,123,456,y=0,z=2,x=9)
def odd():
    n=1
    while True:
        yield n
        n+=2
odd_num = odd()
count = 0
for o in odd_num:
    if count >=5: break
    print(o)
    count +=1