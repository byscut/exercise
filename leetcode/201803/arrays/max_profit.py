# -*- coding: utf-8 -*-
# @Time    : 2018/3/27 下午3:43
# @Author  : Azrael.Bai
# @File    : max_profit.py


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        profit = 0
        flag = 0
        for i in range(1, len(prices)):
            if flag == 0 and prices[i] > prices[i - 1]:
                profit = profit - prices[i - 1]
                flag = 1
            if flag == 1 and prices[i] <= prices[i - 1]:
                profit = profit + prices[i - 1]
                flag = 0
        if flag == 1:
            profit = profit + prices[len(prices) - 1]
        return profit


if __name__ == '__main__':
    s = Solution()
    s.maxProfit([])
