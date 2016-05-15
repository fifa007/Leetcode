#!/usr/bin/env python2.7


'''
Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

For example,
Given n = 3,

You should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
'''


class Solution(object):
    def helper(self, n, level, val, ret):
        n_2 = n * n
        if val > n_2:
            return
        for j in xrange(level, n - level):
            ret[level][j] = val
            val += 1
            if val > n_2:
                return
        for i in xrange(level+1, n-level):
            ret[i][n-level-1] = val
            val += 1
            if val > n_2:
                return
        for j in xrange(n-level-2, level-1, -1):
            ret[n-level-1][j] = val
            val += 1
            if val > n_2:
                return
        for i in xrange(n-level-2, level, -1):
            ret[i][level] = val
            val += 1
            if val > n_2:
                return
        self.helper(n, level+1, val, ret)

    def generate_matrix(self, n):
        if n <= 0:
            return []
        ret = [[0 for j in xrange(n)] for i in xrange(n)]
        self.helper(n, 0, 1, ret)
        return ret