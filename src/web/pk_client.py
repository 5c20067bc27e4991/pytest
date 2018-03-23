import socket
import struct
import mkpack

s = socket.socket()
host = "127.0.0.1"
port = 8888
dataBuf = bytes()

s.connect((host, port))

while True:
    for i in range(5):
        print(i)
        s.send(mkpack.buildPack('cmd', 'os.listdir()'))
    data = s.recv(1024)
    dataBuf += data
    dataType, dataBody, dataBuf = mkpack.recvPack(dataBuf, mkpack.headSize)
    print(dataType, dataBody)
    if not data:
        break
s.close()