#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import os
# import t2

print(time.strftime('%Y-%m-%d %H%M%S', time.localtime()))


def f(a, b=1):
    # print(t2.tt + 444)
    print('This is f function.')
    print('v1=%s,v2=%s' % (a, b))


a = '123'

f_path=input('Input path: ')

print(os.path.exists(f_path))