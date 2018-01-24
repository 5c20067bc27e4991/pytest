# -*- coding: utf-8 -*-
'''
Created on 2017年3月7日
@author: guanglin
'''
import time,sys,os
print(sys.version)
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
print('sys.stdin.encoding==> '+sys.stdin.encoding)
print('sys.stdout.encoding=> '+sys.stdout.encoding) 
print('sys.getdefaultencoding()=> '+sys.getdefaultencoding())
print('sys.getfilesystemencoding()=> '+sys.getfilesystemencoding())

print('你好。')
print(u'你好。')
print('当前目录：'+os.getcwd())
print('当前目录：%s' %(os.getcwd()))
# raw_input(unicode('按任意键继续……','utf-8')) #DOS下乱码
path=r'C:\Users\guanglin\Desktop\test\中文'
if not os.path.exists(path):
    print(str('路径"'+path+'" 不存在!'))
else:
    print('切换至目录'+str(path))
    os.chdir(path)
    print('当前目录：'+os.getcwd())
    print(os.getcwd())
input('按回车继续……')