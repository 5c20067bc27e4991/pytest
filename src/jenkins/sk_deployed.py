#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mkpack
import base64
import json
import hashlib
import os
import shutil
import time
from cmp_code import cmp_dir, decmp_dir
from socketserver import StreamRequestHandler, ThreadingTCPServer
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import MD5

rsa_pub_file = os.path.join(os.path.dirname(os.sys.argv[0]), 'id_rsa.pub')


def veri_sign(rsa_pub_file, cont, signature):
    with open(rsa_pub_file, 'r') as rsa_pub:
        rsa_cont = rsa_pub.read()
    pubKey = RSA.importKey(rsa_cont)
    h = MD5.new(cont.encode('utf-8'))
    verifier = PKCS1_v1_5.new(pubKey)
    return verifier.verify(h, base64.b64decode(signature))


class DeploySvr(StreamRequestHandler):
    def handle(self):
        verified = False
        dataBuf = bytes()
        while True:
            data = self.request.recv(10)
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
                        new_file = open(file_name, 'wb')
                        create_file_flag = False
                    new_file.write(dataBody)
                    new_md5.update(dataBody)
                if dataType == 'fileFin':
                    new_file.close()
                    new_md5 = new_md5.hexdigest()
                    print(file_name + ' received completely.')
                    print('New MD5: ' + new_md5)
                    print('MD5: ' + dataBody)
                    if dataBody == new_md5:
                        print('文件接收成功')
                        self.request.send(mkpack.buildPack('FileOK', '文件接收成功'))
                    else:
                        print('文件接收失败')
                        self.request.send(mkpack.buildPack('FileErr', '文件接收失败'))
                        break

                if dataType == 'cmd':
                    ##data结构[待发布的程序目录, 目标路径]
                    data = json.loads(dataBody)
                    dirs_name = data[0]
                    depl_path = data[1]
                    print(data)
                    ##备份原文件
                    bak_path = os.path.dirname(os.sys.argv[0])
                    bak_file = cmp_dir(depl_path, *dirs_name, bak='Y', cmp_dst_path=bak_path)
                    print('已备份原程序。')
                    ##删除原文件
                    for i in dirs_name:
                        try:
                            shutil.rmtree(os.path.join(depl_path, i))
                        except BaseException:
                            print('删除%s失败！' % i)
                            del_err = '删除%s失败！' % i
                            self.request.send(mkpack.buildPack('Warn', del_err))
                    decmp_dir(file_name, depl_path)
                    # for i in data[2:]:
                    #     try:
                    #         eval(i)
                    #         # print(i)
                    #     except BaseException:
                    #         self.request.send(mkpack.buildPack('CmdErr', i))
                    #         print('CmdErr: ' + i)
                    #         deployErr = True
                    #         break
                    #     self.request.send(mkpack.buildPack('RunFin', i))
                    #     print(i, 'ok')

                    self.request.send(mkpack.buildPack('End', '发布完成'))
                    print('发布完成。')
                    os.remove(file_name)
                    time.sleep(20)
                    os.remove(bak_file)
                    print('已删除备份文件%s。' % os.path.split(bak_file)[-1])


host = '0.0.0.0'
port = 8888
deployed_end = ThreadingTCPServer((host, port), DeploySvr)
deployed_end.serve_forever()
