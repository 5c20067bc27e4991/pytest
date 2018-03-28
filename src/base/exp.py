#!/usr/bin/env python
# -*- coding: utf-8 -*-
for i in range(5):
    try:
        1/0
    except BaseException:
        print(BaseException)
        print("Err")
    else:
        print('OK')