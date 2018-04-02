#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json


def test(a, *t, k1='Y', k2='T'):
    print(a)
    print(t)
    if k1 == 'Y':
        print('Y')
    else:
        print('N')
    if k2 == 'T':
        print('T')
    else:
        print('F')


test(1, 2, 3, 4, k1='xxx')
a = 'hehe'
x = '==>%s' %a
print(x)
