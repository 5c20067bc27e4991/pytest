#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import mkpack
import base64
import json
import os
import time
import hashlib
from socketserver import StreamRequestHandler, ThreadingTCPServer
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import MD5

rsa_pub_file = 'id_rsa.pub'

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


# self.request, addr = s.accept()
class MyServer(StreamRequestHandler):
    def handle(self):
        verified = False
        dataBuf = bytes()
        while True:
            data = self.request.recv(1024)
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
                        self.request.send(mkpack.buildPack('veriOK', '0'))
                        verified = True
                    else:
                        self.request.send(mkpack.buildPack('veriFail', '0'))
                # print(dataType, '--', dataBody)
                if dataType == 'fileStart':
                    file_name = json.loads(dataBody)[0]
                    file_size = json.loads(dataBody)[1]
                    print(file_name, file_size)
                    create_file_flag = True
                if dataType == 'file':
                    if create_file_flag:
                        new_md5 = hashlib.md5()
                        curr_time = time.strftime('%Y%m%d%H%M%S_', time.localtime())
                        new_file = open(curr_time + file_name, 'wb')
                        create_file_flag = False
                    new_file.write(dataBody)
                    new_md5.update(dataBody)
                if dataType == 'fileFin':
                    new_file.close()
                    new_md5 = new_md5.hexdigest()
                    print(file_name + 'received completely.')
                    print('New MD5: ' + new_md5)
                    print('MD5: ' + dataBody)
                    if dataBody == new_md5:
                        print('文件接收成功')
                    else:
                        print('File received wrong.')
                    self.request.send(mkpack.buildPack('End', '0'))

                if dataType == 'cmd':
                    cmds = json.loads(dataBody)
                    print(cmds)
                    for i in cmds:
                        try:
                            eval(i)
                            # print(i)
                        except BaseException:
                            self.request.send(mkpack.buildPack('RunErr', i))
                            print('RunErr: ' + i)
                            break
                        self.request.send(mkpack.buildPack('RunFin', i))
                        print(i, 'ok')
                    self.request.send(mkpack.buildPack('End', '0'))
                    print('End')

host = '0.0.0.0'
port = 8888
deployed_end = ThreadingTCPServer((host, port), MyServer)
deployed_end.serve_forever()