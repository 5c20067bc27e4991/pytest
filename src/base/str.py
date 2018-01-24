# -*- coding: utf-8 -*-
'''
Created on 2017年3月13日
@author: guanglin
'''

str1='Hello,world!'
print 'capitalize()==>',str1.capitalize()
print 'title()==>',str1.title()
print 'upper()==>',(str1.upper())
print 'lower()==>',(str1.lower())
print 'swapcase()==>',(str1.swapcase())

print'ljust()==>\n',(str1.ljust(20))
print'rjust()==>\n',(str1.rjust(20))
print'center()==>\n',(str1.center(20))
print'zfill()==>',str1.zfill(20)
print(str1.find("lo",3,5))
print(str1.rfind("or"))
print(str1.count("o"))
print(str1.index("el"))
print(str1.replace("o","O",2))
print str1.partition(',')

print(str1.startswith("el",1,3))
print(str1.endswith("ll",1,4))
print(str1.isalnum())##全为字母或数字
print(str1.isalpha())
print(str1.isdigit())
print(str1.islower())
print(str1.isupper())
print(str1.istitle())
print 'cmp()==>',(cmp(str1,str1.upper()))
print '-'.join(str1)

str2=' I\'m fine,thank you.Fuck you. '
print(str2.strip())##lstrip() rstrip()
print'strip(str)==>',(str2.strip('Iu. '))
print 'split()==>',str2.split(" ")

str3='a\tb'
print list(str3)
print list(str3.expandtabs())##???
de= str1.decode("gbk")
print(type(de)),'==>',de
en = str1.encode("utf-8")
print(type(en)),'==>',en