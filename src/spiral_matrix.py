#!/usr/bin/env python2.7


'''
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].
'''


class Solution(object):
    def helper(self, matrix, m, n, level, ret):
        p = m * n
        if len(ret) == p:
            return
        for j in xrange(level, n-level):
            ret.append(matrix[level][j])
            if len(ret) == p:
                return
        for i in xrange(level+1, m-level):
            ret.append(matrix[i][n-level-1])
            if len(ret) == p:
                return
        for j in xrange(n-level-2, level-1, -1):
            ret.append(matrix[m-level-1][j])
            if len(ret) == p:
                return
        for i in xrange(m-level-2, level, -1):
            ret.append(matrix[i][level])
            if len(ret) == p:
                return
        self.helper(matrix, m, n, level+1, ret)

    def spiral_matrix(self, matrix):
        if matrix is None or len(matrix) == 0:
            return []
        m = len(matrix)
        n = len(matrix[0])
        ret = []
        self.helper(matrix, m, n, 0, ret)
        return ret