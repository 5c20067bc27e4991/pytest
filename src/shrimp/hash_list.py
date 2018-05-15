#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shutil
import hashlib
import time


def getMD5List(files_path):
    curr_pwd = os.getcwd()
    src_path = files_path
    os.chdir(src_path)
    file_list0 = os.listdir()
    file_list = []
    for i in file_list0:
        if os.path.isfile(i):
            file_list.append(i)

    # print(file_list)
    hash_dict = {}

    for i in file_list:
        with(open(i, 'rb')) as f:
            md5_obj = hashlib.md5()
            md5_obj.update(f.read())
            f_md5 = md5_obj.hexdigest()
        hash_dict[i] = f_md5

    # print(hash_dict)
    with(open('md5.txt', 'w')) as m:
        for i in sorted(hash_dict.items(),key=lambda d:d[1]):
            m.write(i[1] + '\t' + i[0] + '\n')

    os.chdir(curr_pwd)
    return hash_dict


def move_dupl(file_path):
    hash_dict = getMD5List(file_path)
    curr_path = os.getcwd()
    os.chdir(file_path)
    uni_file_list = []
    for i in set(hash_dict.values()):
        for j in hash_dict.keys():
            if hash_dict[j] == i:
                uni_file_list.append(j)
                break

    rep_file_list = list(set(hash_dict.keys()) - set(uni_file_list))
    dupl_size = len(rep_file_list)
    if dupl_size == 0:
        print('No duplicate file.')
        return 0
    # print(rep_file_list)
    curr_time = time.time()
    dupl_dir = 'dupl' + str(round(curr_time))
    os.mkdir(dupl_dir)
    for i in rep_file_list:
        shutil.move(i, dupl_dir)
    os.chdir(curr_path)
    print('Moved %d duplicate files.' % dupl_size)


# getMD5List(r"Z:")
move_dupl(r'Z:')
