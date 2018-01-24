# -*- coding: utf-8 -*-
'''
Created on 2017年3月10日
@author: guanglin
'''

L1=[11,33,22,77]
L2=['ok','hi','Candy','Zoo']

print "id(L1)==>",id(L1)
L1.append(99)
L2.insert(2,'OK')
L1.extend(L2)
L1.remove(11)
print "L1.pop(-2)==>",L1.pop(-2)
L1.reverse()
print 'count()==>',L2.count('ok')
L2.sort()
print "index()==>",L2.index('hi')
print "L1==>",L1
print "L2==>",L2
print id(L1[::-1]),"==>",L1[::-1]
print id(sorted(L1)),"==>",sorted(L1)
r=reversed(sorted(L1))
print "reversed()==>",list(r)
print "reversed()==>",list(r)##迭代器已耗尽
print "id(L1)==>",id(L1)
