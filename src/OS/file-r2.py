#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

l = []
s = bytes()
fn = 'list2.txt'
total_size = os.path.getsize(fn)
read_size = 0
with open(fn, 'rb') as f:
    while read_size < total_size:
        s += f.read(5000)
        read_size += 5

print(s.decode())
with open(fn, 'rb') as f:
    print(f.read(total_size).decode())