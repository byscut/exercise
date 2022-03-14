#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022/3/8 4:39 下午
# @File    : push3.py
# @author  : Akaya
# @Software: PyCharm
# push3  :  it runs ok
import subprocess as sp
import cv2 as cv

rtmpUrl = "rtmp://10.10.14.120/stream/9999"
camera_path = "rtmp://10.10.14.120/stream/2233"
cap = cv.VideoCapture(camera_path)

# Get video information
fps = int(cap.get(cv.CAP_PROP_FPS))
width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

# ffmpeg command
command = ['ffmpeg',
           '-y',
           '-f', 'rawvideo',
           '-vcodec', 'rawvideo',
           '-pix_fmt', 'bgr24',
           '-s', "{}x{}".format(width, height),
           '-r', str(fps),
           '-i', '-',
           '-c:v', 'libx264',
           '-pix_fmt', 'yuv420p',
           '-preset', 'ultrafast',
           '-f', 'flv',
           rtmpUrl]

# 管道配置
p = sp.Popen(command, stdin=sp.PIPE)

# read webcamera
while (cap.isOpened()):
    ret, frame = cap.read()
    if not ret:
        print("Opening camera is failed")
        break

    # process frame
    # your code
    cv.circle(frame, (63, 63), 63, (0, 255, 0), -1)
    cv.line(frame, (350, 400), (500, 500), (0, 0, 255), 3)
    cv.line(frame, (350, 400), (200, 500), (0, 0, 255), 3)
    cv.rectangle(frame, (200, 500), (500, 700), color=(255, 0, 0), thickness=2)
    cv.putText(frame, 'OpenCV2', (10, 200), cv.FONT_HERSHEY_SIMPLEX, 4, (255, 255, 255), 2, cv.LINE_AA)
    # process frame

    # write to pipe
    p.stdin.write(frame.tostring())
