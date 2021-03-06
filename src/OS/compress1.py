# -*- coding: utf-8 -*-
import os
import tarfile
import time

curr_time = time.strftime('%Y%m%d_%H%M%S', time.localtime())
src_outer_dir = 'res'
src_dirs = ('C', 'B', '123.txt','xxx','yyy')
dst_file_name = curr_time + '.tgz'
curr_path = os.getcwd()
cmp_file_full = os.path.join(curr_path, dst_file_name)


def cmp_dir(src_path, dst_path, *src_dirs):
    '''
    不压缩外层目录，只压缩目标文件夹
    '''
    curr_path = os.getcwd()
    os.chdir(src_path)
    curr_time = time.strftime('%Y%m%d_%H%M%S', time.localtime())
    dst_file_full = os.path.join(dst_path, curr_time + '.tgz')
    tar = tarfile.open(dst_file_full, 'w:gz')
    # for i in src_dirs:
    #     for root, dirs, files in os.walk(i):
    #         for file in files:
    #             tar.add(os.path.join(root, file))
    #         for dir in dirs:
    #             tar.add(os.path.join(root, dir))
    ##效果相同
    for i in src_dirs:
        try:
            tar.add(i)
        except FileNotFoundError:
            print('文件'+i+'不存在！')
    tar.close()
    os.chdir(curr_path)


cmp_dir(src_outer_dir, curr_path, *src_dirs)

# os.mkdir(curr_time)
# tar = tarfile.open(dst_cmp_file, 'r')
# for t in tar:
#     tar.extract(t, curr_time)
# tar.close()

