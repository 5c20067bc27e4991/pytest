import socket

s = socket.socket()
host = "127.0.0.1"
port = 8888

s.connect((host, port))
# dst_dir = "C:\\"
# s.send(dst_dir.encode())
# print(s.recv(1024))
for i in range(1001, 1011):
    s.send(str(i).encode())
s.close()
