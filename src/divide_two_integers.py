#!/usr/bin/env python2.7

'''
Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.
'''

MAX_INT = 2147483647
MIN_INT = -2147483648

class Solution(object):
    def divide_integers(self, dividend, divisor):
        if divisor == 0:
            return MAX_INT
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT
        is_negative = False
        if (dividend > 0 > divisor) or (dividend < 0 < divisor):
            is_negative = True
        dvd = abs(dividend)
        dvs = abs(divisor)
        i = 0
        ret = 0
        while dvs << (i+1) <= dvd:
            i += 1
        while dvs <= dvd:
            if dvs << i <= dvd:
                dvd -= dvs << i
                ret += 1 << i
            i -= 1
        return ret if not is_negative else -ret