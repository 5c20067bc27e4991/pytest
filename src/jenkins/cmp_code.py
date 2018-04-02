#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import tarfile
import time


def cmp_dir(src_path, *src_dirs, bak='N', cmp_dst_path='/tmp'):
    '''
    不压缩外层目录，只压缩目标文件夹
    '''
    curr_path = os.getcwd()
    os.chdir(src_path)
    curr_time = time.strftime('%Y%m%d_%H%M%S', time.localtime())
    if bak == 'N':
        dst_file_name = 'src' + curr_time + '.tgz'
    else:
        dst_file_name = 'bak' + curr_time + '.tgz'
    dst_file_full = os.path.join(cmp_dst_path, dst_file_name)
    tar = tarfile.open(dst_file_full, 'w:gz')
    for i in src_dirs:
        try:
            tar.add(i)
        except FileNotFoundError:
            print('文件' + i + '不存在！')

    tar.close()
    os.chdir(curr_path)
    return dst_file_full


def decmp_dir(cmp_file, decmp_dst_path):
    tar = tarfile.open(cmp_file, 'r')
    for t in tar:
        tar.extract(t, decmp_dst_path)
    tar.close()
