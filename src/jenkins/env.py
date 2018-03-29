#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

ENV = os.environ
try:
    branch = ENV['Branch']
except KeyError:
    branch = ''
src_path = ENV['WORKSPACE']
deploy_dirs = tuple(ENV['Deploy_dir'].replace(' ', '').split(','))
dest_host = ENV['Dest_Env'][0]
roll = ENV['Rollback']
print('Deploy_Info: %s %s %s.' % (src_path, deploy_dirs, dest_host))
