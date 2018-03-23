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
headSize = 14


def dataHandle(dataBody):
    # return mkpack.buildPack(dataBody)
    print('Received: ' + dataBody)


def recvData(conn, buf, hsize):
    while True:
        data = conn.recv(1024)
        if not data:
            break
        buf += data
        while True:
            if len(buf) < hsize:
                break
            dataType = struct.unpack(mkpack.structDataType, buf[:hsize])[0]
            bodySize = struct.unpack(mkpack.structDataType, buf[:hsize])[1]

            if len(buf) < hsize + bodySize:
                break

            body = buf[hsize:hsize + bodySize]
            dataHandle(body.decode())

            SD = mkpack.buildPack(dataType.decode(), body.decode())
            conn.send(SD)

            # 粘包处理
            buf = buf[hsize + bodySize:]


conn, addr = s.accept()

recvData(conn, dataBuf, mkpack.headSize)

conn.close()
