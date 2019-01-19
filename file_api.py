# -*- coding:utf-8 -*-

import os, time, json
from datetime import datetime


def get_directory(path_dir):
    file_list = os.listdir(path_dir)
    file_list.sort()
    dir_list = []
    for file in file_list:
        full_name = path_dir+"/"+file
        fileAttr = {}
        fileAttr['name'] = full_name
        fileAttr['updated'] = datetime.fromtimestamp(
            os.path.getmtime(full_name)).strftime("%Y-%M-%d %H:%M:%S")
        fileAttr['created'] = datetime.fromtimestamp(
            os.path.getctime(full_name)).strftime("%Y-%M-%d %H:%M:%S")
        fileAttr['is_dir'] = os.path.isdir(full_name)
        dir_list.append(fileAttr)
    json_string = json.dumps(dir_list, ensure_ascii=False, indent='\t')
    return json_string


def write_file(fileinfo):
    path = fileinfo.get('name')
    is_dir = fileinfo.get('is_dir')
    if is_dir:
        os.mkdir(path)
    else:
        file = open(path, "w")
        file.write(fileinfo.get('text_in_file'))
        file.close()
    print('save_file_ok')
    created = fileinfo.get('created')
    date = datetime.strptime(created, "%Y-%m-%d %H:%M:%S")
    modTime = time.mktime(date.timetuple())
    os.utime(path, (modTime, modTime))
    return fileinfo


def read_file(path):
    file = open(path, "r")
    s = file.read()
    file.close()
    fileAttr = {}
    fileAttr['name'] = path
    fileAttr['updated'] = datetime.fromtimestamp(
        os.path.getmtime(path)).strftime("%Y-%M-%d %H:%M:%S")
    fileAttr['created'] = datetime.fromtimestamp(
        os.path.getctime(path)).strftime("%Y-%M-%d %H:%M:%S")
    fileAttr['text_in_file'] = s
    fileAttr['is_dir'] = False
    json_string = json.dumps(fileAttr, ensure_ascii=False, indent='\t')
    return json_string


if __name__ == '__main__':
    print(read_file("c:/tmp/aaa.txt"))
    save_file("c:/tmp/aaa.txt", "2020-02-20 02:02:02", "hoho")
    get_directory('c:/tmp')
