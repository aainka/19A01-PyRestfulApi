# -*- coding:utf-8 -*-

# 토론토 디렉토리 관리하는 프로그램

import os
import shutil

path_dir = 'U:\토렌토5'
id_list = []

def scan_id():
    for item in file_list:
        if (item.find('@ ')) is not -1 :
            print("+@  "+str(item)[2:])
            id_list.append(str(item)[2:])


def moves(group_id):
    print( " [[[[ "+group_id)
    for item in file_list:
        if (item.find(group_id)) is not -1 :
            file_path = path_dir + "\\"+item
            dst_dir = path_dir+ "\\"+"@ "+group_id
            if ( item.find('@')) is not -1 :
                print("-  "+file_path)
                continue
            
            print("+  "+file_path)
            shutil.move(file_path, dst_dir)

#-----------------------------

file_list = os.listdir(path_dir)
file_list.sort()

scan_id()
for  group_id  in id_list :
    moves(group_id)




