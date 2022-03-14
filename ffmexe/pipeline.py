#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022/3/9 5:33 下午
# @File    : pipeline.py
# @author  : Akaya
# @Software: PyCharm
# pipeline  :  
from ffmpy3 import FFmpeg
import subprocess
ff = FFmpeg(inputs={'pipe:0': '-f rawvideo -pix_fmt rgb24 -s:v 640x480'},
            outputs={'pipe:1': '-c:v h264 -f mp4'})
print(ff.cmd)
stdout, stderr = ff.run(input_data=open('rawvideo', 'rb').read(), stdout=subprocess.PIPE)
