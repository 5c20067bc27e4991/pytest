import socket
import struct
import os
import mkpack
import json

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
    if not data:
        break
    dataBuf += data
    dataType, dataBody, dataBuf = mkpack.recvPack(dataBuf, mkpack.headSize)
    dataHandle(dataType, dataBody)
    # SD = mkpack.buildPack(dataType, dataBody)
    # conn.send(SD)
    print(dataType[:3], dataBody)
    if dataType[:3] == 'cmd':
        print(eval(dataBody))

conn.close()