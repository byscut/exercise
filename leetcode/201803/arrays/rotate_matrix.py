# -*- coding: utf-8 -*-
# @Time    : 2018/3/28 下午4:44
# @Author  : Azrael.Bai
# @File    : rotate_matrix.py


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # matrix[::] = zip(*matrix[::-1]) 最简洁的答案,这tm是什么玩意儿
        length = len(matrix)
        for i in range(0, int(length * 1.0 / 2 + 0.5)):
            for j in range(i, length - i - 1):
                tmp = matrix[length - 1 - j][i]
                matrix[length - 1 - j][i] = matrix[length - 1 - i][length - 1 - j]
                matrix[length - 1 - i][length - 1 - j] = matrix[j][length - 1 - i]
                matrix[j][length - 1 - i] = matrix[i][j]
                matrix[i][j] = tmp

        for lis in matrix:
            print(lis)


if __name__ == '__main__':
    inlist = [
        [5, 1, 9, 11],
        [2, 4, 8, 10],
        [13, 3, 6, 7],
        [15, 14, 12, 16]
    ]
    s = Solution()
    s.rotate(inlist)
