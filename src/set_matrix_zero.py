#!/usr/bin/env python2.7

'''
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.
'''


class Solution(object):
    def set_matrix_zero(self, matrix):
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
            return
        m = len(matrix)
        n = len(matrix[0])
        first_row = False
        first_col = False
        for j in xrange(n):
            if matrix[0][j] == 0:
                first_row = True
                break
        for i in xrange(m):
            if matrix[i][0] == 0:
                first_col = True
                break
        for i in xrange(1, m):
            for j in xrange(1, n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        for i in xrange(1, m):
            if matrix[i][0] == 0:
                for j in xrange(1, n):
                    matrix[i][j] = 0
        for j in xrange(1, n):
            if matrix[0][j] == 0:
                for i in xrange(1, m):
                    matrix[i][j] = 0
        if first_row:
            for j in xrange(n):
                matrix[0][j] = 0
        if first_col:
            for i in xrange(m):
                matrix[i][0] = 0