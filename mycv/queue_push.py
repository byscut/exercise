#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022/3/8 5:21 下午
# @File    : queue_push.py
# @author  : Akaya
# @Software: PyCharm
# queue_push  :  
import queue
import threading
import cv2 as cv
import subprocess as sp


class Live(object):
    def __init__(self):
        self.frame_queue = queue.Queue()
        self.command = ""
        # 自行设置
        self.rtmpUrl = "rtmp://10.10.14.120/stream/9999"
        self.camera_path = "rtmp://10.10.14.120/stream/2233"

    def read_frame(self):
        print("开启推流")
        cap = cv.VideoCapture(self.camera_path)

        # Get video information
        fps = int(cap.get(cv.CAP_PROP_FPS))
        width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

        # ffmpeg command
        self.command = ['ffmpeg',
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
                        self.rtmpUrl]

        # read webcamera
        while (cap.isOpened()):
            ret, frame = cap.read()
            if not ret:
                print("Opening camera is failed")
                # 说实话这里的break应该替换为：
                # cap = cv.VideoCapture(self.camera_path)
                # 因为我这俩天遇到的项目里出现断流的毛病
                # 特别是拉取rtmp流的时候！！！！
                break

            # put frame into queue
            self.frame_queue.put(frame)

    def push_frame(self):
        # 防止多线程时 command 未被设置
        while True:
            if len(self.command) > 0:
                # 管道配置
                p = sp.Popen(self.command, stdin=sp.PIPE)
                break

        while True:
            if self.frame_queue.empty() != True:
                frame = self.frame_queue.get()
                # process frame
                # 你处理图片的代码
                cv.circle(frame, (63, 63), 63, (0, 255, 0), -1)
                cv.line(frame, (350, 400), (500, 500), (0, 0, 255), 3)
                cv.line(frame, (350, 400), (200, 500), (0, 0, 255), 3)
                cv.rectangle(frame, (200, 500), (500, 700), color=(255, 0, 0), thickness=2)
                cv.putText(frame, 'OpenCV', (10, 200), cv.FONT_HERSHEY_SIMPLEX, 4, (255, 255, 255), 2, cv.LINE_AA)
                # write to pipe
                p.stdin.write(frame.tostring())

    def run(self):
        threads = [
            threading.Thread(target=Live.read_frame, args=(self,)),
            threading.Thread(target=Live.push_frame, args=(self,))
        ]
        [thread.setDaemon(True) for thread in threads]
        [thread.start() for thread in threads]
        for t in threads:
            t.join()


if __name__ == '__main__':
    live = Live()
    live.run()
