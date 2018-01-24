# -*- coding: utf-8 -*-
'''
Created on 2017年3月21日
@author: guanglin
'''
import os
# os.O_RDONLY: 以只读的方式打开
# os.O_WRONLY: 以只写的方式打开
# os.O_RDWR : 以读写的方式打开
# os.O_NONBLOCK: 打开时不阻塞
# os.O_APPEND: 以追加的方式打开
# os.O_CREAT: 创建并打开一个新文件
# os.O_TRUNC: 打开一个文件并截断它的长度为零（必须有写权限）
# os.O_EXCL: 如果指定的文件存在，返回错误
# os.O_SHLOCK: 自动获取共享锁
# os.O_EXLOCK: 自动获取独立锁
# os.O_DIRECT: 消除或减少缓存效果
# os.O_FSYNC : 同步写入
# os.O_NOFOLLOW: 不追踪软链接
of=os.open('of.txt', os.O_WRONLY|os.O_CREAT)
os.write(of,'he\nhe')
os.close(of)