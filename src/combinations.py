#!/usr/bin/env python2.7


'''
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
'''


class Solution(object):
    def get_combinations(self, n, k):
        if n == k:
            return [[i for i in xrange(1, n+1)]]
        if k == 1:
            return [[i] for i in xrange(1, n+1)]
        combine1 = self.get_combinations(n-1, k)
        combine2 = self.get_combinations(n-1, k-1)
        combine3 = []
        for comb in combine2:
            combine3.append(comb + [n])
        return combine1 + combine3