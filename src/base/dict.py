# -*- coding: utf-8 -*-
'''
Created on 2017年3月13日
@author: guanglin
'''

d1={'k1':'v1','k2':'v2','k3':'v3'}
d2=d1.copy()
d1['k3']='v33'
d1.update({'k4':'v4','k5':'v5'})
d1['k6']='v6'
print('k1' in d1,'\n')
print('d1.keys()==>',list(d1.keys()),'\n')
print('d1.values()==>',list(d1.values()),'\n')
print('d1.item==>',list(d1.items()),'\n')
del d1['k1']
d3=dict().fromkeys(list(range(5)),'hehe')
print('d3==>',d3,'\n')
d1.setdefault('k88','v88')
print(d1.get('k100',100),'\n')
print(d1)
# d1.clear()
# del d1
# print d1
