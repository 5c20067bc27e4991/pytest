#!/usr/bin/env python
import os
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
            ver_tag = ENV['Tag']
        if 'Revision' in ENV:
            ver_tag = ENV['Revision']
        if 'Input_Revision' in ENV:
            ver_tag = ENV['Input_Revision']
        try:
            ver_tag
        except NameError:
            print('请设置代码Tag或ID！')
            exit(-1)
        print('Ver_Tag: ' + ver_tag)
        os.system('git checkout ' + ver_tag)
