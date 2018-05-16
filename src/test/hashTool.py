#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import base64
import os
import hashlib
import hmac


def Base64():
    print('-----Base64')
    flag_base64 = True
    while flag_base64:
        s = input('请输入需要进行Base64编码的字符串: ').encode()
        b64 = base64.b64encode(s)
        print(b64.decode())
        is_continue = input('Continue("y")?').upper()
        if is_continue == 'Y':
            continue
        else:
            break
    indexMenu()


def MD5(isfile=0):
    print('-----MD5')
    while True:
        if not isfile:
            s = input('请输入需要进行MD5转换的字符串: ').encode()
            md5_obj = hashlib.md5()
            md5_obj.update(s)
            print(md5_obj.hexdigest())
        else:
            f_path = input('请输入需要进行MD5转换的文件路径: ')
            if not os.path.exists(f_path):
                print("File does not exist.\n")
                break
            md5_obj = hashlib.md5()
            with open(f_path, 'rb') as f:
                while True:
                    f_read = f.read(2048)
                    md5_obj.update(f_read)
                    if not f_read:
                        break
            print(md5_obj.hexdigest())
        is_continue = input('Continue("y")?').upper()
        if is_continue == 'Y':
            continue
        else:
            break
    indexMenu()


def sha(sha_bit):
    while True:
        if sha_bit != 256 and sha_bit != 512:
            print('SHA Bit Error.')
            exit(-1)
        s = input('请输入需要进行SHA' + str(sha_bit) + '转换的字符串:').encode()
        sha_obj = eval('hashlib.sha' + str(sha_bit) + '()')
        sha_obj.update(s)
        print(sha_obj.hexdigest())
        is_continue = input('Continue("y")?').upper()
        if is_continue == 'Y':
            continue
        else:
            break

    indexMenu()


def hmacsha256(sha_type):
    while True:
        if sha_type != 256 and sha_type != 512:
            print('SHA Bit Error.')
            exit(-1)
        s = input('请输入需要进行HMACSHA-' + str(sha_type) + '转换的字符串:').encode()
        k = input('请输入密钥: ').encode()
        hm_obj = eval('hmac.new(' + k + ',' + s + 'hashlib.' + sha_type + ')')
        # sha_obj.update(s)
        print(hm_obj.hexdigest())
        is_continue = input('Continue("y")?').upper()
        if is_continue == 'Y':
            continue
        else:
            break

    indexMenu()


def indexMenu():
    hash_method = {0: ['Base64', 'Base64()'], 1: ['MD5', 'MD5()'], 2: ['MD5(file)', 'MD5(1)'],
                   3: ['SHA-256', 'sha(256)'],
                   4: ['SHA-512', 'sha(512)'], 5: ['HMACSHA-256', 'hm(256)'], 6: ['HMACSHA-512', 'hm(512)'],
                   9: ['Quit', 'os._exit(0)']}
    print('-----Hash method-----')
    for i in sorted(hash_method.items(), key=lambda d: d[0]):
        print(i[0], '\t', i[1][0])
    print('-' * 40)
    print('Input hash method code:')

    try:
        ch = int(input())
        # print(hash_method[ch][1])
        eval(hash_method[ch][1])
    except BaseException:
        print('Invalid Code.')
        exit(-1)


indexMenu()
