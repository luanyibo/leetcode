#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
假设你有一个数组，其中第i 个元素是第i天给定股票的价格。

设计一个算法来找到最大的利润。您可以根据需要完成尽可能多的交易（即多次买入和卖出一次股票）。
但是，您不得同时进行多笔交易（即您必须在再次购买之前出售股票）。

text:
[1, 2] max = 1
[2, 1] max = 0
[1, 2, 4] max = 3
[2, 1, 6] max = 5
"""

__author__ = 'Luan Yi Bo'


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # compare near days
        days = len(prices)
        day = 0  # 遍历每一天
        maxProfit = 0  #
        lowDay = 0  # 低价天

        while days:
            if day + 1 > days - 1:
                break
            if prices[day + 1] > prices[lowDay]:
                profit = prices[day + 1] - prices[lowDay]
                maxProfit += profit
            day += 1
            lowDay = day

        return maxProfit
