#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import t2
import t3

print(time.strftime('%Y-%m-%d %H%M%S', time.localtime()))


def f():
    print(t2.tt + 444)


f()
x = t2.t22(100)
print(x)
