# -*- coding: utf-8 -*-
# @Time    : 2018/3/27 下午2:27
# @Author  : Azrael.Bai
# @File    : twosum.py


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        relist = [-1, -1]
        for i in range(0, len(nums)):
            if (target - nums[i]) in nums[i:]:
                other = target - nums[i]
                if nums.index(other) != i:
                    relist = [min(i, nums.index(other)), max(i, nums.index(other))]

        return relist
