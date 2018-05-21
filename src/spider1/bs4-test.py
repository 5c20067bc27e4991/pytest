#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import bs4
from sys import _getframe as GF
from bs4 import BeautifulSoup

# from bs4 import diagnose

with open('test.html', 'r') as f:
    html_init = f.read()
sp = BeautifulSoup(html_init, 'html5lib')
# 解析器可选html.parser lxml lxml-xml xml html5lib

# print(diagnose(html_init))
# print(GF().f_lineno, sp.prettify())
# print(sp.get_text())
# print(sp.getText())
print(GF().f_lineno, sp.title.encode('latin-1'))
print(GF().f_lineno, sp.title.name)
print(GF().f_lineno, sp.div.attrs)
print(GF().f_lineno, sp.option.string)
print(GF().f_lineno, type(sp), ' ---- ', type(sp.div), ' ---- ', type(sp.option.string), ' ---- ', type(sp.a.string))
print(GF().f_lineno, sp.head.contents)
print(GF().f_lineno, sp.title.parent)
[print(GF().f_lineno, p.name) for p in sp.title.parents]
print(GF().f_lineno, sp.option['value'])
print(GF().f_lineno, sp.option.get('value'))
# [print(child.string) for child in sp.body.children if child.name]
# [print(child) for child in sp.body.descendants if child.name]
# [print(child) for child in sp.body.strings]
# [print(child) for child in sp.div.stripped_strings]  # 除去空白
print(GF().f_lineno, sp.find('div'))
print(GF().f_lineno, sp('div'))
print(GF().f_lineno, sp.find_all('div'))
print(GF().f_lineno, sp.find_all(attrs={"class": "c2"}))
print(GF().f_lineno, sp.find_all("div", "c1"))
print(GF().f_lineno, sp.p.next_sibling)
print(sp.body.child)