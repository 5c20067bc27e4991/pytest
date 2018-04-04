#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess

# res = subprocess.check_call('dir', shell=True)
# print(res)
try:
    subprocess.check_call('dir', shell=True)
except:
    print('Cmd Err.')

obj = subprocess.Popen(["dir"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                       universal_newlines=True, shell=True)
obj.stdin.write("print(1)\n")
obj.stdin.write("print(2)")
obj.stdin.close()

cmd_out = obj.stdout.read()
obj.stdout.close()
cmd_error = obj.stderr.read()
obj.stderr.close()

print(cmd_out)
print(cmd_error)
