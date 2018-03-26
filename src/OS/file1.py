# -*- coding: utf-8 -*-
'''
Created on 2017年3月9日
@author: guanglin
Python ver:2.x
'''
import os,chardet
print('Current DIR: '+os.getcwd())
list_file='list.txt'
if not os.path.exists(list_file):
    print('List file "'+list_file+"\" doesn't exist!!!") 
    exit()
fp=open(list_file,'r')
code1=chardet.detect(fp.read())['encoding']
print('list file code: '+code1)
if code1=='windows-1252':
    code2='gbk'
else:
    code2=code1
fp.seek(0)
for line in fp.readlines():
    real_file="res/"+line.decode(code2).strip('\n\r')
    if os.path.exists(real_file):
        print(real_file+" 存在")
    else:
        print(real_file+" 不存在！")
        os.mkdir(real_file)
        print(real_file+" 已创建。")
fp.close()
