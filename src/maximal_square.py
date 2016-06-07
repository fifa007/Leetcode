#!/usr/bin/env python2.7

'''
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing all 1's and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Return 4.
'''


class Solution(object):
    def maximal_square(self, matrix):
        if matrix is None or len(matrix) == 0:
            return 0
        row = len(matrix)
        col = len(matrix[0])
        dp = [[0 for c in xrange(col)] for r in xrange(row)]
        ret = 0
        for i in xrange(row):
            for j in xrange(col):
                if matrix[i][j] == '1':
                    dp[i][j] == 1
                    ret = 1

        for i in xrange(1, row):
            for j in xrange(1, col):
                if matrix[i][j] == '1':
                    dp[i][j] = 1 + min(dp[i-1][j], min(dp[i][j-1], dp[i-1][j-1]))
                    ret = max(ret, dp[i][j])

        return ret * ret