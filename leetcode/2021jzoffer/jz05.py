#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/8/2 4:47 下午
# @File    : jz05.py
# @author  : Bai
# @Software: PyCharm
# jz05 : 替换空格：请实现一个函数，把字符串 s 中的每个空格替换成"%20


class Solution:
    def replaceSpace(self, s: str) -> str:
        return s.replace(' ', "%20")
