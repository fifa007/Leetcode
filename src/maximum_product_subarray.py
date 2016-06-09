#!/usr/bin/env python2.7

'''
Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.
'''

import sys

class Solution(object):
    def max_product(self, nums):
        n = len(nums)
        dp = [[sys.maxsize, -sys.maxsize] for i in xrange(n)]
        dp[0] = [nums[0], nums[0]]
        ret = nums[0]
        for i in xrange(1, n):
            if nums[i] > 0:
                dp[i] = [max(nums[i], dp[i-1][0] * nums[i]), min(nums[i], dp[i-1][1] * nums[i-1])]
            elif nums[i] < 0:
                dp[i] = [max(nums[i], dp[i-1][1] * nums[i]), min(nums[i], dp[i-1][0] * nums[i-1])]
            else:
                dp[i] = [0, 0]
            ret = max(ret, dp[i][0])
        return ret