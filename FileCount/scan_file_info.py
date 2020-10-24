# -*- coding:utf-8 -*-

# 토론토 디렉토리 관리하는 프로그램

import os
import shutil
import os.path

base_dir = 'C:/@DEV/DIV_VisionMgr_R101'

path_dir = 'U:\토렌토5'
scan_dir = 'U:\토렌토5\download'
id_list = []
count = 1
extset = set()

f = open("c:/tmp/div_source.csv", 'w')

#
# FILE SCAN MAIN RECURSION
#

def scan(path):
    global count
    file_list = os.listdir(path)
    for item in file_list:
        fitem = path +'/'+item
        if ( os.path.isdir(fitem)):
            scan(fitem)
        else:
            extname = item.split('.')
            dirlist = fitem[50:].split('/')
            file_check(fitem)

            if ( len(extname) > 1000):
                print("%d,%s,%s,%s,%s"%(count,extname[1],dirlist[0],item,fitem[50:]))
                f.write("%d,%s,%s,%s,%s\n"%(count,extname[1],dirlist[0],item,fitem[50:]))
                count = count + 1
            # if fitem.find('.cpp') > 0 :
            #     print("%s,%s"%(item,fitem[50:]))
        # if ( item.find('.torrent') > 0 ) :
        #     print('Torrent:: %s'%item)
        #     file_path = path_dir + "\\"+item
        #     shutil.move(file_path, path_dir+'\\tor')

# https://yeo0.github.io/pg/2018/11/21/%ED%8C%8C%EC%9D%B4%EC%8D%AC-os.path-%EB%AA%A8%EB%93%88/
def file_check(fullname):
    global count
    size = os.path.getsize(fullname)
    name = os.path.split(fullname) # path, name 분리
    extname = name[1].split('.') # 확장자 분리
    limit = 90*1024*1024
    if ( size > limit):
        print("fullname [%4d] %s    %d "%(count, name[1],size))
        extset.add(extname[1])
        count +=1

   
     

def isFileExt(name, ext):
    sExt = name.split('.')
    print(" ext = ",sExt)

    

def scan_id():
    for item in file_list:
        if (item.find('@ ')) != -1 :
            print("+@  "+str(item)[2:])
            id_list.append(str(item)[2:])
            

def moves(group_id):
    print( "*** find tag = "+group_id)
    file_list = os.listdir(scan_dir)
    for item in file_list:
        if (item.find(group_id)) != -1 :
            file_path = scan_dir + "\\"+item
            dst_dir = path_dir+ "\\"+"@ "+group_id
            if ( item.find('@')) != -1 :
                print("-  "+file_path)
                continue
            print("+  "+file_path)
            if (os.path.exists(dst_dir+"\\"+item)):
                print("file exist -->"+file_path)
                os.remove(file_path)
            else:
                shutil.move(file_path, dst_dir) 

#-----------------------------

print('file scan')
count =1
scan(base_dir)
print('extset=',extset)
f.close()

# file_list = os.listdir(path_dir)
# print('file scan end')
# file_list.sort()

# move_tor()
# scan_id()

# for  group_id  in id_list :
#     moves(group_id)




