# -*- coding: utf-8 -*-
# @Time    : 2018/3/28 下午2:35
# @Author  : Azrael.Bai
# @File    : intersect_2.py


class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dic_nums1 = {}
        for num in nums1:
            if num in dic_nums1.keys():
                dic_nums1[num] += 1
            else:
                dic_nums1[num] = 1

        result_list = []
        for num in nums2:
            if num in dic_nums1.keys():
                if dic_nums1[num] > 0:
                    result_list.append(num)
                    dic_nums1[num] -= 1

        return result_list

