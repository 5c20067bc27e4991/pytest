import socket
import struct
import mkpack

s = socket.socket()
host = "127.0.0.1"
port = 8888
dataBuf = bytes()


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
            print(body)

            SD = mkpack.buildPack(dataType.decode(), body.decode())
            conn.send(SD)

            # 粘包处理
            buf = buf[hsize + bodySize:]


s.connect((host, port))

s.send(mkpack.buildPack('normal', 'hello,world.'))
recvData(s, dataBuf, mkpack.headSize)
s.close()
