#!/usr/bin/env python2.7

'''
Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.
'''


import math

class Solution(object):
    def count_factorial_trailing_zeros(self, n):
        if n <= 0:
            return 0
        ret = 0
        while n > 0:
            ret += math.floor(n / 5)
            n = n / 5

        return ret
