#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import os
import shutil
import uuid
import time

curr_path = os.getcwd()

os.chdir(r'C:\Users\administrator\Desktop\t')
ori_flist = os.listdir('.')
print(ori_flist)
while True:
    ran_file = random.choice(ori_flist)
    bname = os.path.basename(ran_file)
    fname, fsuff = os.path.splitext(bname)
    # curr_time = round(time.time() * 1000)
    # dst_name = fname + '_' + str(curr_time) + fsuff

    dst_name = fname + '_' + str(uuid.uuid1()) + fsuff
    try:
        shutil.copy(ran_file, os.path.join('H:\\', dst_name))
        print(dst_name + ' copied.')
    except BaseException:
        print('Copy completed.')
        break