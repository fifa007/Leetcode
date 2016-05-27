#!/usr/bin/env python2.7


'''
Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.

Note: m and n will be at most 100.
'''


class Solution(object):
    def unique_path(self, nums):
        if nums is None or len(nums) == 0:
            return 0
        m = len(nums)
        n = len(nums[0])
        dp = [[0 for j in xrange(n)] for i in xrange(m)]
        for j in xrange(n):
            if nums[0][j] == 1:
                break
            dp[0][j] = 1
        for i in xrange(m):
            if nums[i][0] == 1:
                break
            dp[i][0] = 1
        for i in xrange(1, m):
            for j in xrange(1, n):
                if nums[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]