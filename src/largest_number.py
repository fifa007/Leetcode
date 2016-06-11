#!/usr/bin/env python2.7


'''
Given a list of non negative integers, arrange them such that they form the largest number.

For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.

'''

class Solution(object):
    def largest_number(self, nums):
        def cmp(x, y):
            sx = str(x) + str(y)
            sy = str(y) + str(x)
            if sx < sy:
                return 1
            elif sx == sy:
                return 0
            return -1

        l = sorted(nums, cmp)
        if l[0] == 0:
            return '0'
        return ''.join(str(i) for i in l)