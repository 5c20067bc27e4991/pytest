#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

lst = list(range(10))
random.shuffle(lst)
print(lst)

for i in range(1, len(lst)):
    tmp = lst[i]
    j = i - 1
    while j >= 0 and lst[j] > tmp:
        lst[j + 1] = lst[j]
        j = j -1
    lst[j + 1] = tmp

print(lst)