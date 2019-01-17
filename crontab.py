# -*- coding:utf-8 -*-


import time

now = time.localtime()
print("time :  %d %d %d "%(now.tm_hour-12, now.tm_min, now.tm_sec))