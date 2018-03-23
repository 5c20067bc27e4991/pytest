#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

s = '\e/a/b/c.txt'
print(os.path.split(s)[1])


def f(a, b):
    return 1, 2

x,y=f(6,8)
print(type(x),y)
print(eval('os.listdir()'))