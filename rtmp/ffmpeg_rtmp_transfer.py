#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/3 10:06 上午
# @File    : rtmp_video_pusher.py
# @author  : Bai
# @Software: PyCharm
import os
import time
from multiprocessing import Process

PULL_ADDR = 'rtmp://localhost:1935/live/1234'
PUSH_ADDR = 'rtmp://10.10.14.120:1935/stream/1234'
TMP_FILE_FOLDER = "./data/"
FILENAME = 'test%d.mp4'
PLAYLIST = 'list.txt'
SEG_TIME = '10'

# -rw_timeout在
# ffmpeg version 4.2.1 Copyright (c) 2000-2019 the FFmpeg developers
#  built with Apple clang version 11.0.0 (clang-1100.0.33.8)
# 构建的程序上无效
# 在 Linux平台 ffmpeg version N-93985-gff2a638-0ubuntu0.16.04.1 Copyright (c) 2000-2019 the FFmpeg developers
# built with gcc 5.4.0 (Ubuntu 5.4.0-6ubuntu1~16.04.11) 20160609
# 上实现有效，其中值 5000000 单位为微妙 即 5s，但是 实际超时时间为 10s
cut_commond = 'ffmpeg -rw_timeout 5000000' \
              ' -i {pull_address}' \
              ' -c copy' \
              ' -flags +global_header' \
              ' -f segment' \
              ' -segment_time {seg_time}' \
              ' -segment_format_options movflags=+faststart' \
              ' -reset_timestamps 1 {filename}'.format(
    pull_address=PULL_ADDR, seg_time=SEG_TIME, filename=TMP_FILE_FOLDER + FILENAME)
push_commond = 'ffmpeg -re -f concat -i {playlist} -c copy -f flv {push_address}'.format(
    playlist=TMP_FILE_FOLDER + PLAYLIST, push_address=PUSH_ADDR)


# p = os.system(cut_commond)
# print(p)

def playlist_generator(max_count):
    str_list = []
    for i in range(0, max_count):
        tuple = 'file \'' + FILENAME % i + '\'\n'
        str_list.append(tuple)
    with open(TMP_FILE_FOLDER + PLAYLIST, 'w') as pl:
        pl.writelines(str_list)


def save_rtmp_video():
    print("save:gene")
    playlist_generator(500)
    print("save:start")
    p = os.system(cut_commond)
    print(p)


def list_rtmp_push():
    print("push:start")
    os.system(push_commond)


if __name__ == '__main__':
    save_process = Process(target=save_rtmp_video)
    push_process = Process(target=list_rtmp_push)
    save_process.start()
    time.sleep(45)  # SLEEP 时间至少要大于 30s + seg_time
    push_process.start()
