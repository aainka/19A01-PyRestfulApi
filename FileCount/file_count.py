# -*- coding:utf-8 -*-

# 토론토 디렉토리 관리하는 프로그램

import os
import shutil

base_dir = 'C:/@DEV/200529_v1863_InnoEyeSimulator_NewUI/trunk'

path_dir = 'U:\토렌토5'
scan_dir = 'U:\토렌토5\download'
id_list = []

def scan(path):
    file_list = os.listdir(path)
    for item in file_list:
        fitem = path +'/'+item
        if ( os.path.isdir(fitem)):
            scan(fitem)
        else:
            if fitem.find('.cpp') > 0 :
                print("%s,%s"%(item,fitem[50:]))
        # if ( item.find('.torrent') > 0 ) :
        #     print('Torrent:: %s'%item)
        #     file_path = path_dir + "\\"+item
        #     shutil.move(file_path, path_dir+'\\tor')

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
scan(base_dir)

# file_list = os.listdir(path_dir)
# print('file scan end')
# file_list.sort()

# move_tor()
# scan_id()

# for  group_id  in id_list :
#     moves(group_id)




