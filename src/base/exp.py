#!/usr/bin/env python
# -*- coding: utf-8 -*-
for i in range(3):
    try:
        assert i != 1, 'i不能为1'
        print(i)
    except AssertionError:
        print('i==1,Error.')
        # exit(-1)
    else:
        print('%s OK' % i)
    finally:
        print('结束第%s轮循环\n-----------' % i)



try:
    raise NameError
except NameError:
    print('\n手动触发NameError')