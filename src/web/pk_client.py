#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import struct
import mkpack
import base64
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import MD5

very_cont = 'Hello'
rsa_file = 'id_rsa'
rsa_pub_file = 'id_rsa.pub'

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


while True:
    s.send(mkpack.buildPack('very_cont', very_cont))
    # for i in range(1, 101):
    #     print(i)
    #     s.send(mkpack.buildPack('cmd' + str(i), 'a' * 50 + '!'))
    data = s.recv(1024)
    dataBuf += data
    while len(dataBuf) >= mkpack.headSize:
        dataType, dataBody, dataBuf = mkpack.recvPack(dataBuf, mkpack.headSize)
        if not dataBody:
            break
        dataType = dataType.strip('\x00')
        print(dataType, dataBody)
s.close()
# exit(0)
