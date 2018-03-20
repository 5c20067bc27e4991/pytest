# -*- coding: utf-8 -*-
'''
Created on 2017年3月20日
@author: guanglin
'''
import os,time,sys
# print repr('a\nb')
def check_exists(ck_file):
    ck_file=ck_file.decode('utf-8').encode('gbk')
    if os.path.exists(ck_file):
        print ck_file.decode('gbk')+' exists.'
        print ck_file+' exists.'
    else:
        print ck_file+' NOT exists!'
    time.sleep(3)
    sys.exit()
# mypath=r'f:\temp'
# mypath=raw_input('input path:').decode('utf-8').encode('gbk')
mypath=raw_input('input path:')
check_exists(mypath)