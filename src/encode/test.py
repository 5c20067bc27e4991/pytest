#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Guanglin
import sys, os, time

i = 100
h = '呵呵'
# print '\n\n',u'%d 你好','%s\n' %(i,u)
print("\n%s\n啦啦\n%d\n" % (h, i))
path_src = input('请输入源路径：').strip('\\')
# path_src_code = path_src.strip('\\')
del_dir = os.path.split(path_src)[0] + '\\deleted' + time.strftime('%Y-%m-%d_%H%M%S', time.localtime())
print(os.path.split(path_src))
print(del_dir)
print(type(del_dir))
