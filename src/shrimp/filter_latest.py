# -*- coding: utf-8 -*-
'''
Created on 2017年3月23日
@author: guanglin
每组文件只保留最新的一个
example: uc_mathematics_lower_secondary_sp2-001-1487229319.scorm.zip
'''

import os,re,shutil,time,sys
path=raw_input('请输入路径：'.decode('utf-8').encode(sys.stdin.encoding)).strip()
if not os.path.isabs(path):
    determine=raw_input('注意：你输入的是相对路径，按回车继续，按其他键退出……'.decode('utf-8').encode(sys.stdin.encoding)).strip()
    if determine:
        print u'程序已退出。'
        sys.exit()
        
if sys.stdin.encoding=='utf-8':
    path_code=path.decode('utf-8').encode('gbk')
else:
    path_code=path
    
if not os.path.exists(path_code):
    print u'路径',path,u'不存在！'
    raw_input('按回车键退出……'.decode('utf-8').encode(sys.stdin.encoding))
    sys.exit()

curr_path=os.getcwd()    
os.chdir(path_code)
ori_list=os.listdir('.')
ch_list=[]
group_list=[]
now_time=time.strftime('%Y-%m-%d_%H_%M_%S',time.localtime())
bak_file='bak'+now_time
if os.path.exists(bak_file):
    time.sleep(2)
    now_time=time.strftime('%Y-%m-%d_%H_%M_%S',time.localtime())
    bak_file='bak'+now_time
os.mkdir(bak_file)

patt='(.*)-(\w+)-(\w+).scorm.zip$'
for ori_file in ori_list:
    if os.path.isfile(ori_file) and re.search(patt, ori_file):
        shutil.move(ori_file, bak_file+'\\'+ori_file)
        f_group=re.search(patt, ori_file).group(2)
        group_list.append(f_group)
        f_timestamp=re.search(patt, ori_file).group(3)
        ch_list.append(f_group+'-'+f_timestamp)
        file_part=re.search(patt, ori_file).group(1)+'-'+'.scorm.zip'
print u'备份完毕，开始筛选最新文件。'

group_list=sorted(list(set(group_list)))
sub_lst=[]
list_result=open('list'+now_time+'.txt','w')
for i in group_list:
    for j in ch_list:
        if i==j.split('-')[0]:
            sub_lst.append(j)            
    max_sub= max(sub_lst)
    latest_file=file_part.split('-')[0]+'-'+max_sub+'.scorm.zip'        
    shutil.copy2(bak_file+'\\'+latest_file,'.')
    list_result.write(latest_file+'\n')
    sub_lst=[]
list_result.close()

os.chdir(curr_path)
print u'已处理完毕，5秒后程序自动退出。'
time.sleep(5)
sys.exit()