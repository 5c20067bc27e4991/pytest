#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

s = '\e/a/b/c.txt'
print(os.path.split(s)[1])

a = 1
i=10

def f():
    return None,None

a,b=f()
print(a)
if not a:
    print('yes')