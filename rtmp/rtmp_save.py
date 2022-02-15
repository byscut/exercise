#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/5/27 4:14 下午
# @File    : rtmp_save.py
# @author  : Bai
# @Software: PyCharm
import ffmpeg

rtmp_str = 'rtmp://10.10.14.120:1935/stream/1234'
# 子进程
(
    ffmpeg
        .input(rtmp_str)
        # 保存的文件名
        .output('saved_rtsp.mp4')
        # 覆盖同名文件
        .overwrite_output()
        # 运行保存
        .run(capture_stdout=True)
)