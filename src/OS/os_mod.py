# -*- coding: utf-8 -*-
'''
Created on 2017年2月27日
@author: guanglin
'''
import os

print("os.sep==>" + os.sep)
print("os.name==>" + os.name)
print("os.getcwd()==>" + os.getcwd())
print("os.curdir==>" + os.curdir)
print("os.listdir()==>")
print(os.listdir('res'))
print("os.getenv()==>" + os.getenv('windir'))
print("os.putenv()==>")
os.putenv('py1', 'myPython')
print(os.stat(os.getcwd()))
# os.system('date')
print("os.linesep==>" + os.linesep)
print("os.path.split()==>")
print(os.path.split(r'f:\temp\c\d.txt'))
print(os.path.splitext("f:/temp/a.txt"))
print(os.path.isfile(r'f:\temp\a.ps21'))
print(os.path.isdir(r'f:\temp'))
print(os.path.exists('c:'))
print(os.path.getsize(r'read.txt'))
print("os.path.abspath()==>" + os.path.abspath('.'))
print(os.path.isabs(r'f:\temp'))
print("os.path.normpath()==>" + os.path.normpath('f:/temp/454343'))
print("os.path.join()==>" + os.path.join(r"f:\temp", r"aa\bb"))
print("os.path.basename()==>" + os.path.basename(r'f:\temp\a.txt'))
print("os.path.dirname()==>" + os.path.dirname(r'f:\temp\a.txt'))
