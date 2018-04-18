#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import os, shutil
import time

curr_path = os.getcwd()

# os.chdir(r'H:\\')
os.chdir(r'C:\Users\guanglin\Desktop\t')
ori_flist = os.listdir('.')
print(ori_flist)
while True:
    curr_time = round(time.time() * 1000)
    ran_file = random.choice(ori_flist)
    bname = os.path.basename(ran_file)
    fname, fsuff = os.path.splitext(bname)
    dst_name = fname + '_' + str(curr_time) + fsuff
    try:
        shutil.copy(ran_file, os.path.join('I:\\', dst_name))
    except BaseException:
        print('Copy completed.')
        break