#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import env
from get_code import rollback
import cmp_code
from decmp_code import decmp_dir


if __name__ == '__main__':
    rollback(env.roll)

    cmp_file_full = cmp_code.cmp_dir(env.src_path, *env.deploy_dirs)

    decmp_dst_path='/tmp/'+os.path.split(cmp_file_full)[1].split('.')[0]
    os.mkdir(decmp_dst_path)
    decmp_dir(cmp_file_full, decmp_dst_path)
