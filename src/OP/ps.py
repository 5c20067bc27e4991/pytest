# -*- coding: utf-8 -*-
'''
Created on 2017年3月21日
@author: guanglin
'''
import psutil
print psutil.version_info
mem=psutil.virtual_memory()
print mem.total,mem.used,psutil.swap_memory()

print psutil.disk_partitions()
print psutil.users()
print psutil.boot_time()
print psutil.pids()
p=psutil.Process(0)
print p.name()
# print p.exe()
print p.status()