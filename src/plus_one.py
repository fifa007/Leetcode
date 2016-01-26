#!/usr/bin/env python2.7


'''
Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.
'''

class Solution(object):
    def plus_one(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits is None or len(digits) == 0:
            return []
        carry_over = 1
        ret = []
        for i in reversed(digits):
            num = i + carry_over
            carry_over = 0
            if num >= 10:
                carry_over = 1
                num %= 10
            ret.insert(0, num)
        if carry_over != 0:
            ret.insert(0, carry_over)

        return ret