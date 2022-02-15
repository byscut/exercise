# -*- coding: utf-8 -*-
# @Time    : 2018/3/28 下午3:02
# @Author  : Azrael.Bai
# @File    : plus_one.py


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        location = len(digits) - 1
        digits[location] += 1
        while location >= 0:
            if digits[location] >= 10:
                if location == 0:
                    digits[location] = digits[location] - 10
                    digits.insert(0, 1)
                    return digits
                digits[location] = digits[location] - 10
                digits[location - 1] += 1
            else:
                break

            location -= 1
        return digits


if __name__ == '__main__':
    s = Solution()
    print(s.plusOne([1, 0]))
