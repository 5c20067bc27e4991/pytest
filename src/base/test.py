# -*- coding: utf-8 -*-
'''
Created on 2017年3月13日
@author: guanglin
'''
def func():
    print('我要在函数内部生成一个函数')
    def func1():
        print('我是函数内部生成好的func1')
    return func1() #返回了一个函数调用,那么在执行这个func的时候，
    #会直接执行func1
    return func1 #返回一个函数对象
myfunc = func()#函数内的局部内容 是不是只能活在函数运行的时候
#myfunc()
print(myfunc)
myfunc
#NameError: name 'func1' is not defined
