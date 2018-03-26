#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import struct
import mkpack
import base64
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import MD5

veri_cont_init = 'Hello'
if len(veri_cont_init) >= 5:
    veri_cont = veri_cont_init[:5]
else:
    veri_cont = veri_cont_init.ljust(5, '0')

rsa_file = 'id_rsa'

s = socket.socket()
host = "127.0.0.1"
port = 8888
dataBuf = bytes()

s.connect((host, port))


def sign(rsa_file, cont):
    with open(rsa_file, 'r') as rsa_key:
        rsa_cont = rsa_key.read()

    priKey = RSA.importKey(rsa_cont)
    signer = PKCS1_v1_5.new(priKey)
    hash_obj = MD5.new(cont.encode('utf-8'))
    signature = base64.b64encode(signer.sign(hash_obj))
    return signature


s.send(mkpack.buildPack('verify', sign(rsa_file, veri_cont).decode('utf-8') + veri_cont))
veri_flag = True
while True:
    data = s.recv(1024)
    dataBuf += data
    while len(dataBuf) >= mkpack.headSize:
        dataType, dataBody, dataBuf = mkpack.recvPack(dataBuf, mkpack.headSize)
        if not dataBody:
            break
        dataType = dataType.strip('\x00')
        if dataType == 'veri_resp' and dataBody == 'Verify failed':
            print('Verify failed.\nConnection closed.')
            veri_flag = False
            break
        if not veri_flag:
            break
        print(dataType, dataBody)
s.close()
# exit(0)
