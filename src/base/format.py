# -*- coding: utf-8 -*-
'''
Created on 2017年3月13日
@author: guanglin
'''
print '{0}-{1}'.format('aa', 'bb')
print '{}-{}'.format('aa', 'bb')
print '{0}-{1}-{0}'.format('aa', 'bb')
print '{name}:{age}'.format(name='Lily',age=18)
class Person():  
    def __init__(self,name,age):  
        self.name,self.age = name,age  
    def __str__(self):  
        return '{self.name},{self.age} years old.'.format(self=self)
print str(Person('Lily',88))
p=['code',123]
print '{0[0]}:{0[1]}'.format(p)
print '{:0>18,.2f}'.format(123456789)
print '================进制转换'
print '{:b}'.format(5)
print '{:d}'.format(5)
print '{:o}'.format(9)
print '{:x}'.format(15)
