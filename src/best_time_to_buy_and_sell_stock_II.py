#!/usr/bin/env python2.7


'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like
(ie, buy one and sell one share of the stock multiple times).
However, you may not engage in multiple transactions at the same time
(ie, you must sell the stock before you buy again).
'''


class Solution(object):
    def max_profit(self, prices):
        if prices is None or len(prices) == 0:
            return 0
        ret = 0
        for i in xrange(1, len(prices)):
            if prices[i] > prices[i-1]:
                ret += prices[i] - prices[i-1]
        return ret