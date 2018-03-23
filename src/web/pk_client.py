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
    for i in range(1, 6):
        print(i)
        s.send(mkpack.buildPack('cmd'+str(i), 'a'*100))
    data = s.recv(2)
    dataBuf += data
    if dataBuf:
        dataType, dataBody, dataBuf = mkpack.recvPack(dataBuf, mkpack.headSize)
        print(dataType, dataBody)

    if not dataBuf:
        print('end')
        break
s.close()
    # exit(0)
