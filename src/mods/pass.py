# -*- coding: utf-8 -*-
'''
Created on 2017年4月1日
@author: guanglin
'''
import getpass
r_input=raw_input("Input:")
print r_input
p_input=getpass.getpass('Pass:')
print p_input
print "Username:",getpass.getuser()
raw_input()