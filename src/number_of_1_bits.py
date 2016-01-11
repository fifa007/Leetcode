#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

'''
Write a function that takes an unsigned integer and
returns the number of ’1' bits it has (also known as the Hamming weight).
For example, the 32-bit integer ’11' has binary representation 00000000000000000000000000001011,
so the function should return 3.
'''


class Solution(object):
    def number_of_1_bits(self, n):
        """
        :type n: int
        :rtype: int
        """
        ret = 0
        while n != 0:
            ret += n & 1
            n >>= 1
        return ret