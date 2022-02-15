# -*- coding: utf-8 -*-
# @Time    : 2018/3/27 下午3:17
# @Author  : Azrael.Bai
# @File    : remove_duplicates.py


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        length = len(nums)
        if length < 1:
            return 0
        for i in range(1, length):
            if nums[i] != nums[count]:
                count += 1
                nums[count] = nums[i]
        return count + 1


if __name__ == '__main__':
    s = Solution()
    r = s.removeDuplicates([1, 1, 2, 2, 3, 3, 3, 3])
    print(r)
