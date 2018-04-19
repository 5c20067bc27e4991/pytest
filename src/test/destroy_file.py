#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

dest_path = 'H:'
os.chdir(dest_path)
for root, dirs, files in os.walk('.'):
    for f in files:
        ori_file = os.path.join(root, f)
        # dst_file = os.path.splitext(ori_file)[0] + '_del' + os.path.splitext(ori_file)[1]
        # os.rename(ori_file, dst_file)
        fill_char = '0' * os.path.getsize(ori_file)
        with open(ori_file, 'w') as d_file:
            d_file.write(fill_char)

    # for d in dirs:
    #     print(os.path.join(root, d))
