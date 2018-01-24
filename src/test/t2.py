#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Guanglin
import sys,os
print(sys.version)
print(sys.getdefaultencoding())
print(sys.stdout.encoding)
print(sys.stdin.encoding)
print(sys.stderr.encoding)

s=r'啦'
print(type(s))
# print(s.decode('utf-8').encode('utf-8'))
print(type(os.getcwd()))
# path=r'C:\Users\guanglin\Desktop\test\中文'
path=r'C:\Users\guanglin\Desktop\test\中文'.decode('utf-8')
print(os.path.exists(path))