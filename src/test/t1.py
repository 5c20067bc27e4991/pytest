# -*- coding: utf-8 -*-
# @Author  : Guanglin
import sys,os

print('Current version: '+sys.version)

# print(u'123呵呵'.encode('utf-8'))
print(u'123啦')
# print(sys.getdefaultencoding())
print(sys.stdin.encoding)
print(sys.stdout.encoding)
print(sys.stderr.encoding)
print(sys.getdefaultencoding())
# print "sys.setdefaultencoding('utf-8')............";reload(sys);sys.setdefaultencoding('utf-8')#不是必须
print(sys.getdefaultencoding())
print(type(u'呵呵'))
print(type('呵呵'))
# print(type('呵呵'.encode('utf-8')))

# print('呵呵'.encode('utf-8'))
print(b'\xe5\x91\xb5'.decode('utf-8'))

# print(type(bytes('123',encoding='utf-8')))
# print(type('呵呵'.decode(sys.stdout.encoding)))
print(unicode('啦啦','utf-8')+u'啦啦')
print(type(r'\abc'))