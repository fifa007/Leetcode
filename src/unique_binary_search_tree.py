#!/usr/bin/env python2.7


'''
Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

For example,
Given n = 3, there are a total of 5 unique BST's.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
'''


class Solution(object):
    def unique_tree(self, n):
        if n <= 1:
            return n
        ret = [0] * (n+1)
        ret[0] = 1
        ret[1] = 1
        for i in xrange(2, n+1):
            for j in xrange(1, i+1):
                ret[i] += ret[j-1] * ret[i-j]
        return ret[n]