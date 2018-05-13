# -*- coding: utf-8 -*-
'''
Created on 2017年3月13日
@author: guanglin
'''


def func():
    print('我要在函数内部生成一个函数')

    global  func1
    def func1():
        print('我是函数内部生成好的func1')



myfunc = func
# myfunc()
print(myfunc())
func1()
# NameError: name 'func1' is not defined
