# -*- coding: utf-8 -*-
# @Time    : 2018/3/27 下午4:46
# @Author  : Azrael.Bai
# @File    : rotate_1.py


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if k == 0:
            return
        if k < 0:
            k = len(nums) - (0 - k) % len(nums)
        else:
            k = k % len(nums)
        if k == 0:
            return
        cop = nums[-k:]
        for i in range(len(nums) - 1, k - 1, -1):
            nums[i] = nums[i - k]
        for i in range(0, k):
            nums[i] = cop[i]


if __name__ == '__main__':
    s = Solution()
    s.rotate([1], 1)
