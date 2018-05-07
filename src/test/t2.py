#!/usr/bin/env python
# -*- coding: utf-8 -*-

tt = 123


def t22(n):
    print('--------')
    print(tt)
    print(n)
    print('--------')
    return 888


print('来自 t2')

from collections import Counter

l = [1, 1, 2, 2, 2, 3, 4, 4, 5]
print(dict(Counter(l)))

d = {'k1': '20', 'k10': '10', 'k2': '2', 'k4': 'v2', 'k5': 'v5', 'k3': 'v1', 'k6': 'v2'}
print(sorted(d))
from operator import itemgetter

print(sorted(d.items(), key=lambda x: itemgetter(1)(x)))
