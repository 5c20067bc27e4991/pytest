# -*- coding: utf-8 -*-
'''
Created on 2017年3月20日
@author: guanglin
'''
import tempfile,os,time,sys
print 'getcwd==>',os.getcwd()
print 'gettempdir()==>',tempfile.gettempdir()
print 'gettempprefix()==>',tempfile.gettempprefix()
print 'mktemp()==>',tempfile.mktemp('.abc','cn_','.')


tmpf=tempfile.mkstemp('.txt', 'CN_', '.')
print tmpf
tfile=os.open(tmpf[1],os.O_WRONLY)
os.write(tfile,time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())+'\n')
os.write(tfile,time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
# tfile=open(tmpf[1],'w')
# tfile.write(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())+'\n')
# tfile.write(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))

os.close(tfile)
os.close(tmpf[0])##需要再次关闭
# tfile.close()

tmpdir=tempfile.mkdtemp('_t', 'Tdir_', '.')
print tmpdir


#创建临时文件，close后自动删除
# tempfile.TemporaryFile(mode, bufsize, suffix, prefix, dir)
TmpFile=tempfile.TemporaryFile('w+b', -1, '.txt', 'Tmp_', '.')
for i in range(5):
    time.sleep(0.5)
    TmpFile.write(str(i))
TmpFile.close()

time.sleep(3)
try:
    os.remove(tmpf[1])
except WindowsError:
    print u"%s 文件正在被使用!" %tmpf[1]
os.rmdir(tmpdir)
print '-'*20
