# -*- coding: utf-8 -*-
'''
Created on 2017年3月10日
@author: guanglin
'''
import os,time,chardet
print('Current DIR: '+os.getcwd())
myfile='write.txt'
fp=open(myfile,'r')
code1=chardet.detect(fp.read())['encoding']
print('File coding:'+str(code1))
fp.close()

fp=open(myfile,'w')
for i in range(5):
    fp.write(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())+'\n')
    time.sleep(0.5)
#     fp.flush()
fp.write('结束。\n')
print('Written.')
fp.close()
##########truncate()
# fp=open(myfile,'r+')
# fp.seek(5)
# fp.truncate(3)
# fp.close()