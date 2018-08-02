#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import time

lst = list(range(10))
random.shuffle(lst)
print(lst)
# t1 = time.time()
for i in range(len(lst) - 1):
    exchange = False
    for j in range(len(lst) - 1 - i):
        if lst[j] > lst[j + 1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]
            exchange = True
    if not exchange:
        break
# t2 = time.time()
# print(t2 - t1)
print(lst)
