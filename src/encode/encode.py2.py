# -*- coding: utf-8 -*-
'''
Created on 2017年3月7日
@author: guanglin
'''
import time,sys,os
print sys.version
print time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
print 'sys.stdin.encoding==> '+sys.stdin.encoding
print 'sys.stdout.encoding=> '+sys.stdout.encoding 
print 'sys.getdefaultencoding()=> '+sys.getdefaultencoding()
print 'sys.getfilesystemencoding()=> '+sys.getfilesystemencoding()
print "sys.setdefaultencoding('gbk')............";reload(sys);sys.setdefaultencoding('gbk')#不是必须
print 'sys.stdin.encoding==> '+sys.stdin.encoding
print 'sys.stdout.encoding=> '+sys.stdout.encoding 
print 'sys.getdefaultencoding()==> '+sys.getdefaultencoding() 
print 'sys.getfilesystemencoding()=> '+sys.getfilesystemencoding() 
print '你好，DOS.'#DOS下乱码
print unicode('呵呵。','utf-8')
print u'1当前目录：'+os.getcwd()
print u'2当前目录：%s' %os.getcwdu()
path=r'C:\Users\guanglin\Desktop\test\中文'.decode('utf-8')
if not os.path.exists(path):
    print u'路径"'+path+u'" 不存在!'
else:
    print u'切换至目录'+path
    os.chdir(path)
    print u'3当前目录：'+os.getcwdu()
print(type(raw_input(u'按回车继续……'.encode(sys.stdout.encoding))))