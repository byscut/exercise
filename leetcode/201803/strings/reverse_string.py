# -*- coding: utf-8 -*-
# @Time    : 2018/3/29 上午10:06
# @Author  : Azrael.Bai
# @File    : reverse_string.py


class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]


if __name__ == '__main__':
    s = Solution()
    print(s.reverseString("abcdefg"))
