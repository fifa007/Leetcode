#!/usr/bin/env python2.7


'''
Given two sparse matrices A and B, return the result of AB.

You may assume that A's column number is equal to B's row number.

Example:

A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]


     |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                  | 0 0 1 |
Show Company Tags
Show Tags

'''

class Solution(object):
    def multiplication(self, A, B):
        if A is None or len(A) == 0 or B is None or len(B) == 0:
            return []
        m, n = len(A), len(B[0])
        k = len(A[0])
        ret = [[0 for j in xrange(n)] for i in xrange(m)]
        for i in xrange(m):
            for l in xrange(k):
                if A[i][l] != 0:
                    for j in xrange(n):
                        if B[l][j] == 0: continue
                        ret[i][j] += A[i][l] * B[l][j]
        return ret