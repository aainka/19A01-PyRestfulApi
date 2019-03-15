# -*- coding:utf-8 -*-

# CmdHandler를 이식하기 위한 프로그램
# TACS 개발하면서 사용함.

import os
import shutil

path_dir = 'S:\sw-dev\eclipse-workspace-18b\TmpHandler'
handlerNames = []

def scan_id():
    file_list = os.listdir(path_dir)
    cnt = 0
    for item in file_list:
        if (item.find('XX_')) is not -1 :
            continue
        if (item.find('ESM')) is not -1 :
            continue    
        if (item.find('.java')) is not -1 :
            handlerNames.append(item)
            cnt = cnt+1
            print(cnt,item)

def proc_file(filename):
    print("proc => ",filename)
    file = open(path_dir+'\\'+filename, 'r')
    s = file.read()
    line = s.split('\n')
    file.close()
    r=""
    for eline in line:
        if (eline.find('import') is not -1):
            continue
        if (eline.find('lgnortel') is not -1):
            r = r+"package com.cmd.handler;\n"
            r = r+"import com.cmd.AbstractCommandHandler;\n"
            r = r+"import com.cmd.CommandType;\n"
            r = r+"import com.cmd.ParamType;\n"  
            r = r+"import java.util.ArrayList;\n" 
            r = r+"import com.cmd.DBManager;\n" 
            r = r+"import java.util.List;\n"
            continue
        r = r + eline+'\n'
    spath = 'S://sw-dev//eclipse-workspace-18b//19A02-R2-TACS-SUP//src//main//java//com//cmd//handler//'
    file = open(spath+filename, 'w')
    file.write(r)
    file.close()

def all_proc():
    for item in handlerNames:
        proc_file(item)

def all_table():
    count = 0
    s=""
    for item in handlerNames:
        count = count +1
        s =  s + "new " +item[0:-5]+ "(),"
        if count % 5 == 0:
            print(s)
            s=""

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

scan_id()
#all_proc()
all_table()
#proc_file('C9950Handler.java')
# file_list.sort()

# scan_id()
# for  group_id  in id_list :
#     moves(group_id)