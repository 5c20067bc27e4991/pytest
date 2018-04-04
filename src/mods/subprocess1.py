#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess

# res = subprocess.check_call('dir', shell=True)
# print(res)
try:
    subprocess.check_call('dir',shell=True)
except:
    print('Cmd Err.')