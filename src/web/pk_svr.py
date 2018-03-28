#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import mkpack
import base64
import json
import os
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import MD5

rsa_pub_file = 'id_rsa.pub'
s = socket.socket()
host = '0.0.0.0'
port = 8888
s.bind((host, port))
s.listen(5)

dataBuf = bytes()


def veri_sign(rsa_pub_file, cont, signature):
    with open(rsa_pub_file, 'r') as rsa_pub:
        rsa_cont = rsa_pub.read()
    pubKey = RSA.importKey(rsa_cont)
    h = MD5.new(cont.encode('utf-8'))
    verifier = PKCS1_v1_5.new(pubKey)
    return verifier.verify(h, base64.b64decode(signature))


def dataHandle(dataType, dataBody):
    print('Type: ' + dataType)
    print('Body: ' + dataBody)


conn, addr = s.accept()
verified = False
while True:
    data = conn.recv(1024)
    dataBuf += data
    while len(dataBuf) >= mkpack.headSize:
        dataType, dataBody, dataBuf = mkpack.recvPack(dataBuf, mkpack.headSize)
        if not dataBody:
            break
        dataType = dataType.strip('\x00')
        if not verified:
            if dataType == 'verify':
                signature = dataBody[:-5]
                veri_cont = dataBody[-5:]
            if veri_sign(rsa_pub_file, veri_cont, signature):
                conn.send(mkpack.buildPack('veriOK', '0'))
                verified = True
            else:
                conn.send(mkpack.buildPack('veriFail', '0'))

        if dataType == 'cmd':
            cmds = json.loads(dataBody)
            print(cmds)
            for i in cmds:
                try:
                    eval(i)
                    # print(i)
                except BaseException:
                    conn.send(mkpack.buildPack('RunErr', i))
                    print('RunErr: ' + i)
                    break
                conn.send(mkpack.buildPack('RunFin', i))
                print(i, 'ok')
            conn.send(mkpack.buildPack('End', '0'))

# print(dataBody)
# conn.send(mkpack.buildPack('Ret', dataBody))

conn.close()
