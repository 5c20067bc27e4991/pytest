#!/usr/bin/env python
# -*- coding: utf-8 -*-
import t2
import time

print(time.strftime('%Y-%m-%d %H%M%S',time.localtime()))
def f():
    print(t2.tt + 444)
d={'a':'b'}

try:
    print(d['c'])
except KeyError:
    print('KE')

x=''
if not x:
    print(99999)