#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import struct
import mkpack
import base64
import uuid
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
    prikey = RSA.importKey(rsa_cont)
    signer = PKCS1_v1_5.new(prikey)
    hash_obj = MD5.new(cont.encode('utf-8'))
    signature = base64.b64encode(signer.sign(hash_obj))
    return signature


veriNo = str(uuid.uuid1())
s.send(mkpack.buildPack('verify', sign(rsa_file, veri_cont).decode('utf-8') + veri_cont + veriNo))
veri_ok = False
BK = False
while True:
    data = s.recv(1024)
    dataBuf += data
    while len(dataBuf) >= mkpack.headSize:
        dataType, dataBody, dataBuf = mkpack.recvPack(dataBuf, mkpack.headSize)
        if not dataBody:
            break
        dataType = dataType.strip('\x00')
        if dataType == 'veriFail' and veriNo == dataBody[-36:]:
            print('Verify failed.\nConnection closed.')
            BK = True
            break
        if dataType == 'veriOK' and veriNo == dataBody[-36:]:
            veri_ok = True

        if veri_ok:
            if veriNo == dataBody[-36:]:
                send_uuid = str(uuid.uuid1())
                s.send(mkpack.buildPack('cmd', 'os.listdir()' + send_uuid))
            if dataType == 'RunErr':
                print('Run failed: ' + dataBody[:-36])
                print('Run failed: ' + dataBody)
                BK = True
                break
            if dataType == 'RunFin' and send_uuid == dataBody[-36:]:
                send_uuid = str(uuid.uuid1())
                # print(dataBody[:-36] + 'Run completely.')
                print(dataBody + 'Run completely.')
                s.send(mkpack.buildPack('cmd', 'print("hehehe")' + send_uuid))
            if dataType == 'RunFin' and send_uuid == dataBody[-36:]:
                send_uuid = str(uuid.uuid1())
                # print(dataBody[:-36] + 'Run completely.')
                print(dataBody + 'Run completely.')
                print('Over')
                BK = True
                veri_ok = False
                break
    if BK:
        break

s.close()
