#!/usr/bin/env python2.7


'''
You are given coins of different denominations and a total amount of money amount.
Write a function to compute the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:
coins = [1, 2, 5], amount = 11
return 3 (11 = 5 + 5 + 1)

Example 2:
coins = [2], amount = 3
return -1.

Note:
You may assume that you have an infinite number of each kind of coin.
'''


class Solution(object):
    def coin_change(self, coins, amount):
        if coins is None:
            return -1
        INF = 0x7ffffffe
        dp = [INF] * (amount+1)
        dp[0] = 0
        for i in xrange(amount+1):
            for c in coins:
                if c + i <= amount:
                    dp[c+i] = min(dp[c+i], dp[i] + 1)

        return dp[amount] if dp[amount] != INF else -1