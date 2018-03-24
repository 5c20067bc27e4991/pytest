#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import struct
import os
import mkpack

s = socket.socket()
host = '0.0.0.0'
port = 8888
s.bind((host, port))
s.listen(5)

dataBuf = bytes()


def dataHandle(dataType, dataBody):
    # return mkpack.buildPack(dataBody)
    print('Type:' + dataType)
    print('Body: ' + dataBody)


conn, addr = s.accept()

while True:
    data = conn.recv(1024)
    print('DATA==>', data.decode())
    dataBuf += data
    while len(dataBuf) >= mkpack.headSize:
        dataType, dataBody, dataBuf = mkpack.recvPack(dataBuf, mkpack.headSize)
        if not dataBody:
            break
        dataType = dataType.strip('\x00')
        # print(dataType, dataBody)
        print('len databuf:', len(dataBuf))
        if dataType[:3] == 'cmd':
            print(dataType)
            # print(eval(dataBody))
            # print(dataBody)
            # conn.send(mkpack.buildPack('Ret', dataBody))

conn.close()
