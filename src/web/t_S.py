#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from socketserver import StreamRequestHandler, ThreadingTCPServer


class MyServer(StreamRequestHandler):
    def handle(self):
        rev = self.request.recv(1024)
        print('From ', self.request)
        self.request.send(rev)
        print(rev)
        print(self.client_address)



s1 = ThreadingTCPServer(('127.0.0.1', 9999), MyServer)
s1.allow_reuse_address = True
s1.serve_forever()
