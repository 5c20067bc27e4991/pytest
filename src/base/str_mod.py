# -*- coding: utf-8 -*-
'''
Created on 2017年3月13日
@author: guanglin
'''
import string

intab='abc'
outtab='123'
trantab=string.maketrans(intab, outtab)
str1='It is a cat!'
print str1.translate(trantab,'is')
print string.ascii_letters
print 'ascii_lowercase==>',string.ascii_lowercase
print string.ascii_uppercase
print string.digits
print string.hexdigits
print string.letters
print string.lowercase
print string.uppercase
print string.octdigits
print 'punctuation==>',string.punctuation
print list(string.printable)
print list(string.whitespace)

tmp=string.Template('Hello,${var}.')
map={'var':'Tom'}
print tmp.substitute(map)
