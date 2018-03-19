# -*- coding:utf-8 -*-

from socketserver import ThreadingTCPServer, StreamRequestHandler
import struct
import subprocess


class MyRequestHandler(StreamRequestHandler):
    def handle(self):

        while True:
            print("connect from:", self.client_address)
            cmd = bytes.decode(self.request.recv(1024))
            if not cmd: break
            res = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            err = res.stderr.read()
            if err:
                back_msg = err
            else:
                back_msg = res.stdout.read()

            self.request.send(struct.pack("i", len(back_msg)))
            self.request.send(back_msg)


if __name__ == '__main__':
    tcp_Server = ThreadingTCPServer(("127.0.0.1", 8081), MyRequestHandler)
    tcp_Server.allow_reuse_address = True
    tcp_Server.serve_forever()
