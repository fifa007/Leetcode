#!/usr/bin/env python2.7


'''
Given an integer, write a function to determine if it is a power of three.
Follow up:
Could you do it without using any loop / recursion?
'''

from math import floor
from math import log

class Solution(object):
    def is_power_of_three(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        p = int(floor(log(n) / log(3)))
        power_floor = pow(3, p)
        power_ceil = power_floor * 3
        if power_floor == n or power_ceil == n:
            return True
        return False