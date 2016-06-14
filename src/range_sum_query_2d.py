#!/usr/bin/env python2.7

'''
Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper
left corner (row1, col1) and lower right corner (row2, col2).

Range Sum Query 2D
The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3),
which contains sum = 8.

Example:
Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12
Note:
You may assume that the matrix does not change.
There are many calls to sumRegion function.
You may assume that row1 ≤ row2 and col1 ≤ col2.

'''


class Solution(object):
    def __init__(self, matrix):
        if matrix is None or len(matrix) == 0:
            return
        m = len(matrix)
        n = len(matrix[0])
        self.dp = [[0 for j in xrange(n)] for i in xrange(m)]
        self.dp[0][0] = matrix[0][0]
        for j in xrange(1, n):
            self.dp[0][j] = self.dp[0][j-1] + matrix[0][j]
        for i in xrange(1, m):
            self.dp[i][0] = self.dp[i-1][0] + matrix[i][0]
        for i in xrange(1, m):
            for j in xrange(1, n):
                self.dp[i][j] = self.dp[i-1][j] + self.dp[i][j-1] - \
                    self.dp[i-1][j-1] + matrix[i][j]

    def range_sum(self, row1, col1, row2, col2):
        ret = self.dp[row2][col2]
        if col1 > 0:
            ret -= self.dp[row2][col1-1]
        if row1 > 0:
            ret -= self.dp[row1-1][col2]
        if col1 > 0 and row1 > 0:
            ret += self.dp[row1-1][col1-1]
        return ret