#!/usr/bin/env python2.7

'''
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
'''

class Solution(object):
    def single_number(self, nums):
        ret = 0
        for num in nums:
            ret = ret ^ num
        return ret