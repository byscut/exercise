#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022/3/9 10:53 上午
# @File    : trans_video.py
# @author  : Akaya
# @Software: PyCharm
# trans_video  :  
from ffmpy3 import FFmpeg
ff = FFmpeg(inputs={'/Users/baiyang/Downloads/export.mp4': None},
            outputs={'/Users/baiyang/Downloads/output.ts': '-c:a mp2 -c:v mpeg2video'})
print(ff.cmd)
ff.run()
