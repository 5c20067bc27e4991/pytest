#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import mkpack
import base64
import json
import time
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import MD5

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


cmds = ['os.listdir()', 'print("hehe1")', 'print("hehe2")']
s = socket.socket()
host = "127.0.0.1"
port = 8888
dataBuf = bytes()
s.connect((host, port))

s.send(mkpack.buildPack('verify', sign(rsa_file, veri_cont).decode('utf-8') + veri_cont))
veri_ok = False
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
        if dataType == 'veriFail':
            print('Verify failed.\nConnection closed.')
            BK = True
            break
        if dataType == 'veriOK':
            veri_ok = True
            cmd_flag = True

        if veri_ok:
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
                print('Task completed.', dataBody)
                time.sleep(5)
                BK = True
                break
    if BK:
        break

s.close()
