#!/usr/bin/env python2.7


'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit.
You may complete as many transactions as you like
(ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:

prices = [1, 2, 3, 0, 2]
maxProfit = 3
transactions = [buy, sell, cooldown, buy, sell]
'''


class Solution(object):
    def max_profit(self, prices):
        n = len(prices)
        if n <= 1:
            return 0
        sells = [None] * n
        buys = [None] * n
        sells[0], sells[1] = 0, max(0, prices[1] - prices[0])
        buys[0], buys[1] = -prices[0], max(-prices[0], -prices[1])
        for i in xrange(2, n):
            sells[i] = max(buys[i-1] + prices[i], sells[i-1])
            buys[i] = max(buys[i-1], sells[i-2] - prices[i])
        return sells[-1]