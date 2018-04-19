# -*- coding: utf-8 -*-
'''
@author: guanglin
'''
import os

# p = input('Input path: ')
p = 'res'
os.chdir(p)
for root, dirs, files in os.walk('.'):
    for f in files:
        print(os.path.join(root, f))
    for d in dirs:
        print(os.path.join(root, d))