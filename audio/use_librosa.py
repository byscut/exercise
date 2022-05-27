#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022/4/18 2:58 下午
# @File    : test_librosa.py
# @author  : Akaya
# @Software: PyCharm
# test_librosa  :
import librosa

y, sr = librosa.load('test_audio.mp3', sr=None)
print(sr)
melspec = librosa.feature.melspectrogram(y, sr, n_fft=1024, hop_length=512, n_mels=128)
logmelspec = librosa.power_to_db(melspec)
print(logmelspec.shape)

mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40)
print(mfccs.shape)
