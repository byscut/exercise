#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/8/2 4:11 下午
# @File    : jz04.py
# @author  : Bai
# @Software: PyCharm
# jz04 : 二维数组中查找：在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个高效的函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
from typing import List


class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        rs = len(matrix)
        if rs == 0:
            return False
        cs = len(matrix[0])
        row = 0
        col = cs - 1
        while row < rs and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                row += 1
            else:
                col -= 1
        return False
