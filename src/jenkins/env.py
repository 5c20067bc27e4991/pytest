#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

ENV = os.environ
src_path = ENV['WORKSPACE']
deploy_dirs = tuple(ENV['Deploy_dir'].split(','))
dest_host = ENV['Dest_Env'][0]
roll = ENV['Rollback']
print('Deploy_Info: %s %s %s.' % (src_path, deploy_dirs, dest_host))
