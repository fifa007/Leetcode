#!/usr/bin/env python2.7


'''
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

For example, given the range [5, 7], you should return 4.
'''


class Solution(object):
    def range_bitwise_and(self, m, n):
        r = 0
        while m != n:
            m >>= 1
            n >>= 1
            r += 1
        return r << m