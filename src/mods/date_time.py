# -*- coding: utf-8 -*-
'''
Created on 2017年3月21日
@author: guanglin
'''
import time,datetime

print('time()==>',time.time())
print('mktime()==>',time.mktime(time.localtime()))

print('gmtime()==>',time.gmtime())
print('localtime()==>',time.localtime())

print('strptime()==>',time.strptime('2017-3-21','%Y-%m-%d'))
print('strftime()==>',time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))

print('ctime()==>',time.ctime(time.time()))
print('asctime()==>',time.asctime(time.localtime()))

print(datetime.datetime.now())
dt=datetime.datetime(2017,3,23,20,15,18)
print(dt)
print('fromtimestamp()==>',datetime.datetime.fromtimestamp(time.time()))
print('utcfromtimestamp()==>',datetime.datetime.utcfromtimestamp(time.time()))
print(dt.timetuple())
print(dt.strftime('%Y-%m-%d %H'))
