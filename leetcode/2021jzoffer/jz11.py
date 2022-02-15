#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/8/3 4:23 下午
# @File    : jz11.py
# @author  : Akaya
# @Software: PyCharm
# jz11  :  旋转数组：把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。
from typing import List


class Solution:
    def minArray(self, numbers: List[int]) -> int:
        if numbers[0] < numbers[-1]:
            return numbers[0]
        for n in numbers:
            if (n < numbers[0]): return n
        return numbers[0]


class Solution2:
    def minArray(self, numbers: List[int]) -> int:
        left, right = 0, len(numbers) - 1
        mid = 0
        while left <= right:
            mid = left + (right - left) // 2
            if numbers[mid] > numbers[right]:
                left = mid + 1
            elif numbers[mid] < numbers[right]:
                right = mid
            else:
                right -= 1
        return numbers[mid]
