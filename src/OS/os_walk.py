# -*- coding: utf-8 -*-
'''
@author: guanglin
'''
import os

# p = input('Input path: ')
p = 'res'
for dirpath, dirname, filename in os.walk(p):
    for f in filename:
        print(os.path.join(dirpath, f))
    for d in dirname:
        print(os.path.join(dirpath, d))
