#!/usr/bin/env python2.7

'''
Given a triangle, find the minimum path sum from top to bottom.
Each step you may move to adjacent numbers on the row below.

For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space,
where n is the total number of rows in the triangle.
'''


class Solution(object):
    def min_total(self, triangle):
        dp = [0 for i in xrange(triangle)]
        n = len(triangle)
        for row in xrange(n):
            old_dp = dp[:]
            for j in xrange(len(triangle[row])):
                if j == 0:
                    dp[j] = old_dp[j] + triangle[row][j]
                elif j == len(triangle[row]) - 1:
                    dp[j] = old_dp[j-1] + triangle[row][j]
                else:
                    dp[j] = min(old_dp[j], old_dp[j-1]) + triangle[row][j]

        return min(dp)