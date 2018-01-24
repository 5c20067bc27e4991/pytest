# -*- coding: utf-8 -*-
'''
Created on 2017年4月1日
@author: guanglin
'''
import os
fileDir = "." + os.sep + ".." 
i=0
for root, dirs, files in os.walk(fileDir):
    print root
    print dirs
    print files
    print '*'*20
    i=i+1
    if i==5:
        break