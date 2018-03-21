# -*- coding:utf-8 -*-

import socket
import struct

host = "127.0.0.1"
port = 8081

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

while True:
    cmd = input(">>>>").strip()
    if not cmd:
        continue
    s.send(cmd.encode("utf-8"))

    package_len = s.recv(4)
    package_size = struct.unpack("i", package_len)[0]

    recv_size = 0
    recv_bytes = b""

    while recv_size < package_size:
        res = s.recv(1024)
        recv_bytes += res
        recv_size += len(res)
print(recv_bytes.decode('utf-8'))

s.close()
