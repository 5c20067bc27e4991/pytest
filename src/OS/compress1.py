# -*- coding: utf-8 -*-
import os
import tarfile
import time

curr_time = time.strftime('%Y%m%d_%H%M%S', time.localtime())
src_path = 'res'
dst_cmp_file = curr_time + '.tgz'
curr_path = os.getcwd()
cmp_file_full = os.path.join(curr_path, dst_cmp_file)

##不压缩外层目录，只压缩目标文件和目录
os.chdir(src_path)
tar = tarfile.open(cmp_file_full, 'w:gz')
for dirpath, dirname, filename in os.walk('.'):
    for f in filename:
        tar.add(os.path.join(dirpath, f))
        print('add--' + os.path.join(dirpath, f))
    for d in dirname:
        tar.add(os.path.join(dirpath, d))
        print('add--' + os.path.join(dirpath, d))
##效果相同
# for i in os.listdir():
#     tar.add(i)
tar.close()
os.chdir(curr_path)
os.mkdir(curr_time)
tar = tarfile.open(dst_cmp_file, 'r')
for t in tar:
    tar.extract(t, curr_time)
tar.close()
