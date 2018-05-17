#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import _getframe as GF
from bs4 import BeautifulSoup

with open('test.html', 'r') as f:
    html_init = f.read()
sp = BeautifulSoup(html_init, 'html5lib')

# print(sp.get_text())
# print(sp.getText())
print(GF().f_lineno, sp.title)
print(GF().f_lineno, sp.title.name)
print(GF().f_lineno, sp.title.string)
print(GF().f_lineno, sp.title.parent.name)
print(GF().f_lineno, sp.option['value'])
print(GF().f_lineno, sp.option.attrs)
print(GF().f_lineno, sp.find('div'))
print(GF().f_lineno, sp('div'))
print(GF().f_lineno, sp.find_all('div'))
print(GF().f_lineno, sp.find_all("div", "c1"))
print(GF().f_lineno, sp.find_all(attrs={"class": "c1"}))
