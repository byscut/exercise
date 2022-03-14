#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022/3/8 3:37 下午
# @File    : cv_push.py
# @author  : Akaya
# @Software: PyCharm
# cv_push  : pipeline push
import subprocess as sp
import cv2
import sys
import queue
import threading

frame_queue = queue.Queue()
rtmpUrl = "rtmp://10.10.14.120/stream/9999"
camera_path = "rtmp://10.10.14.120/stream/2233"  # 'rtmp://58.200.131.2:1935/livetv/hunantv'  # 这是湖南台的实时直播流

# 获取摄像头参数
cap = cv2.VideoCapture(camera_path)
fps = int(cap.get(cv2.CAP_PROP_FPS))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

print(fps, width, height)

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
           '-g', '5',
           rtmpUrl]


# 读流函数
def Video():
    vid = cv2.VideoCapture(camera_path)
    if not vid.isOpened():
        raise IOError("could't open webcamera or video")
    while (vid.isOpened()):
        ret, frame = vid.read()
        # 下面注释的代码是为了防止摄像头打不开而造成断流
        # if not ret:
        # vid = cv2.VideoCapture(camera_path）
        # if not vid.isOpened():
        # raise IOError("couldn't open webcamera or video")
        # continue
        frame_queue.put(frame)


def push_stream(left_x, left_y, right_x, right_y):
    # 管道配置
    while True:
        if len(command) > 0:
            p = sp.Popen(command, stdin=sp.PIPE)
            break

    while True:
        if not frame_queue.empty():
            frame = frame_queue.get()
            if frame is not None:
                # 我这里出现了frame为NoneType的情况，所以判断一下
                image = cv2.resize(frame[int(left_x):int(right_x)][int(left_y):int(right_y)], (width, height))
                p.stdin.write(image.tostring())


def run(left_x, left_y, right_x, right_y):
    thread_video = threading.Thread(target=Video, )
    thread_push = threading.Thread(target=push_stream, args=(left_x, left_y, right_x, right_y,))
    thread_video.start()
    thread_push.start()


if __name__ == "__main__":
    run(0, 0, 720, 1280)
