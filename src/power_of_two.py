#!/usr/bin/env python2.7


'''
Given an integer, write a function to determine if it is a power of two.
'''


class Solution(object):
    def is_power_of_two(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        return n & (n - 1) == 0