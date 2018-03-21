#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tarfile
import os
import cmp_code

def decmp_dir(cmp_file, decmp_dst_path):
    tar = tarfile.open(cmp_file, 'r')
    for t in tar:
        tar.extract(t, decmp_dst_path)
    tar.close()
