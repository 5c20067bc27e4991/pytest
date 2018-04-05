# -*- coding: utf-8 -*-
'''
Created on 2017年2月28日
@author: guanglin
'''
import os, shutil

print('当前路径：' + os.getcwd())
path = r'res'
os.chdir(path)
print('当前路径：' + os.getcwd())

# os.mkdir('tmpdir')
# os.makedirs(r'a/b/c')
# os.rmdir('tmpdir') # 删除空目录
# os.removedirs("a/b/c") # 递归删除空目录
# shutil.rmtree('tmpdir')
# os.remove('a.txt')
# os.unlink('dir/test')   #删除文件

# os.rename('x', 'A')#重命名文件、目录
# shutil.move('123', 'A') # 移动或重命名文件/目录，目标路径不能已经存在
# shutil.copyfile('123.txt', 'd\d.txt') #复制文件，需写明目标文件名，若目标文件存在则覆盖
# shutil.copy('123.txt', 'd') #可复制文件到目录，若目标文件存在则覆盖
# shutil.copy2('a.txt', r'dst') #在copy基础上复制最后访问、修改时间
# shutil.copymode('c', 'd') #仅复制文件/目录权限
# shutil.copystat('src', 'dst2') #仅复制文件/目录权限、最后访问、修改时间
# shutil.copytree('a', 'd\ccc')  #复制目录,目标路径不能已经存在
# print(os.stat('123.txt'))
# print os.stat('dst2')
