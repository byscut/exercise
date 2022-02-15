#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/8/3 3:26 下午
# @File    : jz10-1.py
# @author  : Akaya
# @Software: PyCharm
# jz10-1  :  斐波那契数列：写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项（即 F(N)）
from functools import lru_cache


class Solution:
    @lru_cache(None)
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        result = self.fib(n - 1) + self.fib(n - 2)
        while result > 1000000007:
            result -= 1000000007
        return result
