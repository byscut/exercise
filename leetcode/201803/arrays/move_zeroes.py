# -*- coding: utf-8 -*-
# @Time    : 2018/3/28 下午3:35
# @Author  : Azrael.Bai
# @File    : move_zeroes.py


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(0, len(nums) - 1):
            if nums[i] == 0:
                j = i
                while j < len(nums) and nums[j] == 0:
                    j += 1
                if not j == len(nums):
                    nums[i] = nums[j]
                    nums[j] = 0
                else:
                    break

        print(nums)


if __name__ == '__main__':
    s = Solution()
    s.moveZeroes([0, 1, 0, 3, 12])
