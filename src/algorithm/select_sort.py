#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

lst = list(range(10))
random.shuffle(lst)
print(lst)

for i in range(len(lst) - 1):
    min_loc = i
    for j in range(i+1, len(lst)):
        if lst[j] < lst[min_loc]:
            min_loc = j
    lst[min_loc], lst[i] = lst[i], lst[min_loc]

print(lst)
