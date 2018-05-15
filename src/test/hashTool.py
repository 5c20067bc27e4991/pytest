#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import base64

s = 'this is a example'.encode()
b64 = base64.b64encode(s)


def indexMenu():
    hash_method = {0: 'Base64', 1: 'MD5', 2: 'MD5(file)', 3: 'SHA-256', 4: 'SHA-512', 5: 'HMACSHA-256',
                   6: 'HMACSHA-512'}
    print('-----Hash method-----')
    for i in sorted(hash_method.items(), key=lambda d: d[0]):
        print(i[0], '\t', i[1])
    print('-' * 40)
    print('Input hash method code:')

    try:
        ch = int(input())
        print(hash_method[ch])
    except BaseException:
        print('Invalid Code.')
        exit(-1)


indexMenu()


def md5(cont, isfile=0):
    pass


def sha256(cont):
    pass


def sha512(cont):
    pass


def hmacsha256(cont):
    pass


def hmacsha512(cont):
    pass
