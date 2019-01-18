# -*- coding:utf-8 -*-

import os
import time
from datetime import datetime
import json


def get_directory(path_dir):
    print("### path_dir=%s"%path_dir)
    file_list = os.listdir(path_dir)
    file_list.sort()
    dir_list = []
    for file in file_list:
        full_name = path_dir+"/"+file
        fileAttr = {}
        fileAttr['name'] = file
        time.asctime
        fileAttr['updated'] = datetime.fromtimestamp(
            os.path.getmtime(full_name)).strftime("%Y-%M-%d %H:%M:%S KST")
        fileAttr['created'] = datetime.fromtimestamp(
            os.path.getctime(full_name)).strftime("%Y-%M-%d %H:%M:%S KST")
        fileAttr['is_dir'] = os.path.isdir(full_name)
        dir_list.append(fileAttr)
    json_string = json.dumps(dir_list, ensure_ascii=False, indent='\t')
    return json_string


def save_file(path, created, content):
    file = open(path, "w")
    file.write(content)
    file.close()
    print('save_file_ok')
    date = datetime.strptime(created, "%Y-%m-%d %H:%M:%S")
    modTime = time.mktime(date.timetuple())
    os.utime(path,(modTime,modTime))
    # file = open(“testfile.text”, “r”)
    # print file.read()
    return


def read_file(path):
    print('read_file.path = ',path)
    file = open(path, "r")
    s = file.read()
    file.close()
    return s


if __name__ == '__main__':
    print(read_file("c:/tmp/aaa.txt"))
    save_file("c:/tmp/aaa.txt", "2020-02-20 02:02:02", "hoho")
    get_directory('c:/tmp')
