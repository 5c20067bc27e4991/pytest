# -*- coding: utf-8 -*-
'''
Created on 2017年3月7日
@author: guanglin
'''
import sys,os,shutil,chardet,time
print('Current DIR: '+os.getcwd())
parent_path=r'C:\Users\guanglin\git\shrimp_py\src\os\\'
cnt_file=parent_path+r'read2.txt'
if not os.path.exists(cnt_file):
    print(cnt_file+'不存在。')
    os._exit(1)
print('文件大小：%d字节' %os.path.getsize(cnt_file))
fp=open(cnt_file,'r')
myline=fp.read()
fcode=chardet.detect(myline)['encoding']
print('File encoding:'+fcode)
if fcode != 'utf-8':
    fcode='gbk'
print('sys.stdin.encoding==>'+sys.stdin.encoding)
fp.close()
########read()
# fp=open(cnt_file,'r')
# myline=fp.read()
# fcode=chardet.detect(myline)['encoding']
# print 'File coding:'+fcode
# fp.seek(0)
# print '====='+cnt_file+'=====\n'+myline+'\n=========='
# for line in myline:
#     print line
# fp.close()
############迭代
fp=open(cnt_file,'r')
for i in fp:
    print(i.strip('\n\r').decode(fcode).encode(sys.stdin.encoding))
fp.close()
#########readline()
# fp=open(cnt_file,'r')
# # fp.seek(15,0)
# myline=fp.readline()
# while myline:
# #     print fp.tell()
#     print myline.strip('\r\n')
#     myline=fp.readline()
# fp.close()
##########readlines()
# fp=open(cnt_file,'r')
# 
# lines=fp.readlines()
# for myline in lines:
#     print myline.strip('\r\n')
# fp.close()
time.sleep(3)