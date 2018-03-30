#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import env
from get_code import rollback, get_branch
from cmp_code import cmp_dir
# from decmp_code import decmp_dir
import sk_jk

if __name__ == '__main__':
    br = env.branch.split('/')[-1]
    get_branch(br)
    rollback(env.roll)

    cmp_file_full = cmp_dir(env.src_path, *env.deploy_dirs)
    cmp_filename = os.path.basename(cmp_file_full)

    cmd2_decmp = "decmp_code.decmp_dir('" + cmp_filename + "',r'" + env.dest_path + "')"

    cmd_list = ['os.listdir()', cmd2_decmp, 'print("cmd3")']
    sk_jk.sock_jk(env.dest_host, cmp_file_full, cmd_list)
    print('')

    # decmp_dst_path = '/tmp/' + os.path.split(cmp_file_full)[1].split('.')[0]
    # os.mkdir(decmp_dst_path)
    # decmp_dir(cmp_file_full, decmp_dst_path)
