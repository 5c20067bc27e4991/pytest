#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import env
import time
from get_code import rollback, get_branch
from cmp_code import cmp_dir
import sk_jk

if __name__ == '__main__':
    t_start = time.time()

    br = env.branch.split('/')[-1]
    get_branch(br)
    rollback(env.roll)

    cmp_file_full = cmp_dir(env.src_path, *env.deploy_dirs)
    cmp_filename = os.path.basename(cmp_file_full)

    cmd2_decmp = "decmp_dir('" + cmp_filename + "',r'" + env.dest_path + "')"
    ##data结构[待发布的程序目录, 目标路径]
    # cmd_list = [env.deploy_dirs, env.dest_path, 'os.listdir()', cmd2_decmp, 'print("cmd3")']
    data_list = [env.deploy_dirs, env.dest_path]
    sk_jk.sock_jk(env.dest_host, cmp_file_full, data_list)
    t_end = time.time()
    print('共耗时%s秒。' % (t_end - t_start))

    # decmp_dst_path = '/tmp/' + os.path.split(cmp_file_full)[1].split('.')[0]
    # os.mkdir(decmp_dst_path)
    # decmp_dir(cmp_file_full, decmp_dst_path)
