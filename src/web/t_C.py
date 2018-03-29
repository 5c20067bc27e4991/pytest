#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket

host = "127.0.0.1"
port = 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
s.send('hello'.encode())
print(s.recv(1024))
s.close()