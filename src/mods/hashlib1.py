#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib
from Crypto.Hash import MD5

str1 = 'hello'
str2 = 'world'
md5_1 = hashlib.md5()
md5_1.update(str1.encode())
md5_1.update(str2.encode())
md5_2 = hashlib.md5((str1 + str2).encode())
print('MD5_1: ' + md5_1.hexdigest())
print('MD5_2: ' + md5_2.hexdigest())

hash_obj = MD5.new((str1 + str2).encode('utf-8'))
print(hash_obj.digest())