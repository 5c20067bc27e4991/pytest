#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import struct
import mkpack

s = socket.socket()
host = "127.0.0.1"
port = 8888
dataBuf = bytes()

s.connect((host, port))

while True:
    for i in range(1, 101):
        print(i)
        s.send(mkpack.buildPack('cmd'+str(i), 'a'*50+'!'))
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
