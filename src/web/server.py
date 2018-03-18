import socket
import os

s = socket.socket()
host = '0.0.0.0'
port = 8888
s.bind((host, port))
s.listen(5)

i = 1
conn, addr = s.accept()
while True:
    # print("Client Addr: ", addr)
    # recv_dir = conn.recv(2014)
    # print("Recv_dir: ", recv_dir)
    # print("list dir==> ", os.listdir(recv_dir))
    # conn.send("caocaocao".encode('utf8'))
    # print(conn.recv(100))
    data = conn.recv(4)
    if not data:
        break
    print(str(i) + " ==> " + data.decode())
    i += 1
conn.close()
