#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import os
import shutil
import uuid
import time


def fill_disk(src_path, dst_path):
    curr_path = os.getcwd()

    src_path = os.path.join(os.environ['USERPROFILE'], src_path)
    file_list = os.listdir(src_path)
    while True:
        rand_file = random.choice(file_list)
        src_file = os.path.join(src_path, rand_file)
        fname, fsuff = os.path.splitext(rand_file)
        # curr_time = round(time.time() * 1000)
        # dst_name = fname + '_' + str(curr_time) + fsuff
        dst_name = fname + '_' + ''.join(str(uuid.uuid1()).split('-')) + fsuff
        try:
            shutil.copy(src_file, os.path.join(dst_path, dst_name))
            print(dst_name + ' copied.')
        except BaseException:
            print('Copy completed.')
            break
        os.chdir(curr_path)


src = r'Desktop\t'
dst = 'Y:\\'
fill_disk(src, dst)
