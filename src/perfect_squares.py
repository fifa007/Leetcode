#!/usr/bin/env python2.7


'''
Given a positive integer n, find the least number of
perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.
'''

import math

class Solution(object):
    def num_of_squares(self, n):
        while n % 4 == 0:
            n /= 4
        if n % 8 == 7:
            return 4
        a = 0
        while a*a <= n:
            b = int(math.sqrt(n - a*a))
            if a*a + b*b == n:
                if a > 0 and b > 0:
                    return 2
                else:
                    return 1
            a += 1
        return 3