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

d = {'k1': 'v1', 'k2': 'v2', 'k3': 'v1', 'k4': 'v2', 'k5': 'v5', 'k6': 'v2'}
uni_key = []
uni_val = set(d.values())
for v in uni_val:
    for k in d.keys():
        if d[k] == v:
            uni_key.append(k)
            break
print(uni_key)
print(set(d.keys()) - set(uni_key))

# for k, v in d.items():
#     print(k, v)
