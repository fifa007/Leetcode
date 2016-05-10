#!/usr/bin/env python2.7

'''
Given an array of integers, every element appears three times except for one. Find that single one.
'''


class Solution(object):
    def single_number(self, nums):
        ret = 0
        for i in xrange(32):
            sum = 0
            x = (1 << i)
            for j in xrange(len(nums)):
                if x & nums[j]:
                    sum += 1
            if sum % 3 != 0:
                if i == 31:
                    ret -= (1 << 31)
                else:
                    ret |= x
        return ret