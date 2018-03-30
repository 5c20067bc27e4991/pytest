#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, sys

print('Curr path', os.getcwd())
pro_path = os.path.dirname(sys.argv[0])
print('Py pro dir ==>', pro_path)
if os.path.exists(os.path.join(pro_path, '1.txt')):
    print('1.txt exists')
else:
    print('1.txt does not exist')

input()
