#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Guanglin
import sys,os
import locale,chardet
# print(locale.getdefaultlocale())
path=raw_input(u'请输入路径：'.encode(sys.stdin.encoding))
print chardet.detect(path)
path=path.decode(sys.stdin.encoding)
print u'你输入的路径是 ',path
print(os.path.exists(path))
print(type(path))