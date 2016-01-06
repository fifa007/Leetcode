#!/usr/bin/python2.7

'''
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime?
'''


class Solution(object):
    def add_digits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return num
        i = num / 9
        if num == 9 * i:
            return 9
        if num > i * 9:
            return num - 9 * i