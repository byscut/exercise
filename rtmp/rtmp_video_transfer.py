#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/5/27 4:55 下午
# @File    : rtmp_test.py
# @author  : Bai
# @Software: PyCharm
import cv2 as cv
import subprocess as sp


def run_opencv_camera():
    video_stream_path = 0
    # 当video_stream_path = 0 会开启计算机 默认摄像头  也可以为本地视频文件的路径
    cap = cv.VideoCapture(video_stream_path)

    while cap.isOpened():
        is_opened, frame = cap.read()
        cv.imshow('frame', frame)
        cv.waitKey(1)
    cap.release()


PULL_ADDR = 'rtmp://localhost:1935/live/1234'
PUSH_ADDR = 'rtmp://10.10.14.120:1935/stream/1234'
cap = cv.VideoCapture(PULL_ADDR)

# Get video information
fps = int(cap.get(cv.CAP_PROP_FPS))
width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

# ffmpeg command
command = ['ffmpeg',
        '-y',
        '-f', 'rawvideo',
        '-vcodec','rawvideo',
        '-pix_fmt', 'bgr24',
        '-s', "{}x{}".format(width, height),
        '-r', str(fps),
        '-i', '-',
        '-c:v', 'libx264',
        '-pix_fmt', 'yuv420p',
        '-preset', 'ultrafast',
        '-f', 'flv',
        PUSH_ADDR]

# 管道配置
p = sp.Popen(command, stdin=sp.PIPE)

# read webcamera
while(cap.isOpened()):
    ret, frame = cap.read()
    if not ret:
        print("Opening camera is failed")
        break

    # process frame
    # your code
    # process frame

    # write to pipe
    p.stdin.write(frame.tostring())


if cap.isOpened():
    cap.read()