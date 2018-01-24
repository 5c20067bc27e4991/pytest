# -*- coding: utf-8 -*-
'''
Created on 2017年3月20日
@author: guanglin
'''
import random,string
print 'random()==>'
for i in range(5):
    print random.random(),
    
print '\n\nuniform()==>'
for i in range(5):
    print random.uniform(10,12),
    
print '\n\nrandint()==>'
for i in range(5):
    print random.randint(10,12),
    
print '\n\nrandrange()==>'
for i in range(5):
    print random.randrange(10,14,2),
    
print '\n\nchoice()==>'
for i in range(5):
    print random.choice('Hello'),
    
print '\n\nshuffle()==>'
lst=[1,2,3,4,5,6,7,8,9]
random.shuffle(lst)
print lst

print '\n\nsample()==>'
lst=[1,2,3,4,5,6,7,8,9]
print random.sample(lst,5)
print lst
