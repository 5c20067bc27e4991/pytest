# -*- coding: utf-8 -*-
'''
Created on 2017年4月1日
@author: guanglin
'''
import fabric,datetime
def hello():
    print u'你好hello'
    fabric.api.local('ls')
    print datetime.datetime.now()