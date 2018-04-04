#!/usr/bin/env python
import os
import subprocess
from env import ENV


def get_branch(br):
    if not br:
        print('未选择分支，默认获取主干代码。')
        os.system('git checkout master')
        os.system('git pull')


    else:
        print('已选择分支' + br)
        os.system('git checkout ' + br)
        os.system('git pull')


def rollback(roll):
    '''
    回滚处理
    '''
    if roll == 'true':
        if 'Tag' in ENV:
            ver_tag = ENV['Tag']
        if 'Input_Tag' in ENV:
            ver_tag = ENV['Input_Tag']
        if 'Revision' in ENV:
            ver_tag = ENV['Revision']
        if 'Input_Revision' in ENV:
            ver_tag = ENV['Input_Revision']
        try:
            ver_tag
        except NameError:
            print('请设置代码Tag或ID！')
            exit(-1)
        try:
            subprocess.check_call(['git', 'checkout', ver_tag])
        except:
            print('选择版本时出现错误,中止发布。')
            exit(-1)