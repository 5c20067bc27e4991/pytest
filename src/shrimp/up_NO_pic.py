# -*- coding: utf-8 -*-
'''
Created on 2017年3月15日
@author: guanglin
##更新资源保留原缩略图
'''
import sys,os,chardet,time,shutil

print u'“源路径”指新资源所在的路径。'
print u'“目标路径”指需要被更新的旧资源所在路径。'
print '===================='
path_src=raw_input(u'请输入源路径：'.encode(sys.stdin.encoding)).strip('\\')
path_dst=raw_input(u'请输入目标路径：'.encode(sys.stdin.encoding)).strip('\\')
list_file=raw_input(u'请输入list文件完整路径：'.encode(sys.stdin.encoding)).strip()

#文件操作，路径编码转为unicode

path_src_code=path_src.decode(sys.stdin.encoding)
path_dst_code=path_dst.decode(sys.stdin.encoding)
list_file_code=list_file.decode(sys.stdin.encoding)


if not os.path.exists(path_src_code):
    print u'源路径',path_src,u'不存在！'
    raw_input(u'按回车键退出……'.encode(sys.stdin.encoding))
    sys.exit()
# print path_src,u'内容:'
# for src_ls in os.listdir(path_src_code):
#     print src_ls.decode('gbk')
    
if not os.path.exists(path_dst_code):
    print u'目标路径',path_dst,u'不存在！'
    raw_input(u'按回车键退出……'.encode(sys.stdin.encoding))
    sys.exit()

if not os.path.isfile(list_file_code):
    print list_file,u'文件不存在。'
    raw_input(u'按回车键退出……'.encode(sys.stdin.encoding))
    sys.exit()

if path_src_code == path_dst_code:
    print u'源路径和目标路径相同，请检查后重新输入。'
    raw_input(u'按回车键退出……'.encode(sys.stdin.encoding))
    sys.exit()
        
# print u'list文件:',list_file
f_list=open(list_file_code,'r')
fcode=chardet.detect(f_list.read())['encoding']
# print 'File encoding:',fcode
if fcode != 'utf-8':
    fcode= 'gbk'
f_list.seek(0)
list_all=[]
for list_line in f_list:
    list_line=list_line.strip(' \n\r')
    list_line_encode=list_line.decode(fcode).encode(sys.stdin.encoding)
    if not list_line:
        continue
    if list_line not in os.listdir(path_src_code):
        print u'源路径 ',path_src,u'中没有文件',list_line_encode
        raw_input(u'按回车键退出……'.encode(sys.stdin.encoding))
        sys.exit()
    if list_line not in os.listdir(path_dst_code):
        print u'目标路径 ',path_dst,u'中没有文件',list_line_encode
        raw_input(u'按回车键退出……'.encode(sys.stdin.encoding))
        sys.exit()
    list_all.append(list_line)
f_list.close()

del_dir=os.path.split(path_dst_code)[0]+'\\deleted'+time.strftime('%Y-%m-%d_%H%M%S',time.localtime())
if not os.path.exists(del_dir):
    os.mkdir(del_dir)
#将png从目标路径复制至源路径
png_max='thumbnail.png'
png_min='thumbnail_s.png'
i=0
for each_list in list_all:
    shutil.copy(path_dst_code+'\\'+each_list+'\\'+png_max,path_src_code+'\\'+each_list)
    shutil.copy(path_dst_code+'\\'+each_list+'\\'+png_min,path_src_code+'\\'+each_list)
#将目标路径下的旧目录移至备份目录
    shutil.move(path_dst_code+'\\'+each_list, del_dir)
#将源路径的目录复制至目标路径
    shutil.copytree(path_src_code+'\\'+each_list, path_dst_code+'\\'+each_list)
    i=i+1
    print each_list.decode(fcode).encode(sys.stdin.encoding),u'已更新' 
print u'\n共%d个资源目录被更新,旧文件已备份至%s。\n' %(i,del_dir)
raw_input(u'按回车键退出……'.encode(sys.stdin.encoding))