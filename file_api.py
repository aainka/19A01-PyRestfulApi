# -*- coding:utf-8 -*-

import os
import time
import datetime 
import json

def get_directory(path_dir):
    file_list = os.listdir(path_dir)
    file_list.sort()
    dir_list = []
    for file in file_list:
        fileAttr = {}
        fileAttr['name'] = file
        time.asctime
        fileAttr['updated'] = datetime.datetime.fromtimestamp(os.path.getmtime(path_dir+file)).strftime("%Y-%M-%d %I:%M:%S KST")
        fileAttr['created'] = datetime.datetime.fromtimestamp(os.path.getmtime(path_dir+file)).strftime("%Y-%M-%d %I:%M:%S KST")
        fileAttr['is_dir'] = os.path.isdir(path_dir+file)
        dir_list.append(fileAttr)
    json_value = json.dumps(dir_list, ensure_ascii=False, indent='\t')
    print(json_value)
    return json_value

def read_file(path_dir):
    print('xx')
    return

     

if __name__ == '__main__':
    get_directory('c:/')