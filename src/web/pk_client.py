#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import mkpack
import base64
import json
import time
import os
import hashlib
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import MD5

t_start = time.time()
veri_cont_init = 'Hello'
if len(veri_cont_init) >= 5:
    veri_cont = veri_cont_init[:5]
else:
    veri_cont = veri_cont_init.ljust(5, '0')

rsa_file = 'id_rsa'


def sign(rsa_file, cont):
    with open(rsa_file, 'r') as rsa_key:
        rsa_cont = rsa_key.read()
    prikey = RSA.importKey(rsa_cont)
    signer = PKCS1_v1_5.new(prikey)
    hash_obj = MD5.new(cont.encode('utf-8'))
    signature = base64.b64encode(signer.sign(hash_obj))
    return signature


code_file = r'C:\Users\guanglin\Desktop\1.zip'
if os.path.exists(code_file):
    file_size = os.path.getsize(code_file)
else:
    print(code_file, ' does not exist.')

cmds = ['os.listdir()', 'print("hehe1")', 'print("hehe2")']
s = socket.socket()
host = "127.0.0.1"
port = 8888
dataBuf = bytes()
s.connect((host, port))

s.send(mkpack.buildPack('verify', sign(rsa_file, veri_cont).decode('utf-8') + veri_cont))
veri_ok = False
send_file_flag = False
cmd_flag = False
BK = False

while True:
    data = s.recv(1024)
    dataBuf += data
    while len(dataBuf) >= mkpack.headSize:
        dataType, dataBody, dataBuf = mkpack.recvPack(dataBuf, mkpack.headSize)
        if not dataBody:
            break
        dataType = dataType.strip('\x00')
        ##签名验证
        if dataType == 'veriFail':
            print('Verify failed.\nConnection closed.')
            BK = True
            break
        if dataType == 'veriOK':
            veri_ok = True
            send_file_flag = True

        if veri_ok:
            ##发送文件
            if send_file_flag:
                sent_size = 0
                rem_size = 0
                send_once = 5000
                md5 = hashlib.md5()
                s.send(mkpack.buildPack('fileStart', json.dumps([os.path.split(code_file)[-1], file_size])))
                with open(code_file, 'rb') as cf:
                    while sent_size < file_size:
                        rem_size = file_size - sent_size
                        send_size = send_once if rem_size > send_once else rem_size
                        send_b = cf.read(send_size)
                        s.send(mkpack.buildPack('file', send_b))
                        md5.update(send_b)
                        sent_size += send_size
                        print(sent_size, '/', file_size)
                md5 = md5.hexdigest()
                s.send(mkpack.buildPack('fileFin', md5))
                print('File sent.')
                send_file_flag = False
                # cmd_flag = True

            ##发送命令
            if cmd_flag:
                s.send(mkpack.buildPack('cmd', json.dumps(cmds)))
                cmd_flag = False
            if dataType == 'RunErr':
                print('Run failed: ' + dataBody)
                BK = True
                break
            if dataType == 'RunFin':
                print(dataBody + ' Run completed.')
            if dataType == 'End':
                print('Task completed.')
                BK = True
                break
    if BK:
        break

s.close()
t_end = time.time()
print('Took %s seconds' %(t_end - t_start))
