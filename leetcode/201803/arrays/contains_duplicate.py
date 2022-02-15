# -*- coding: utf-8 -*-
# @Time    : 2018/3/27 下午5:29
# @Author  : Azrael.Bai
# @File    : contains_duplicate.py


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) <= 1:
            return False
        hash_list = {}
        for i in range(0, len(nums)):
            key = nums[i] % 100
            if key not in hash_list.keys():
                hash_list[key] = [nums[i]]
            else:
                if nums[i] in hash_list[key]:
                    return True
                else:
                    hash_list[key].append(nums[i])
        return False

    def bubbleSort(self, nums):
        for i in range(len(nums) - 1):  # 这个循环负责设置冒泡排序进行的次数
            for j in range(len(nums) - i - 1):  # ｊ为列表下标
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        return nums


if __name__ == '__main__':
    s = Solution()
    print(s.containsDuplicate([3, 3]))
