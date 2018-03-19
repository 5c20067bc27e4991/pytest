# -*- coding: utf-8 -*-
'''
Created on 2017年3月22日
@author: guanglin
'''
import pickle
cont=[123,'hello','hehe']
pdump=pickle.dumps(cont)
pload=pickle.loads(pdump)

print('pickle.dumps ==> %r' %pdump)
print('pickle.loads ==> %r' %pload)


ptxt=open('pk.txt','wb')
pickle.dump(cont,ptxt)
ptxt.close()

print('\nLoad from pickle.txt:')
pread=open('pk.txt','r')
print(pickle.load(pread))
pread.close()