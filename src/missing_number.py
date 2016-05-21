#!/usr/bin/env python2.7


'''
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n,
find the one that is missing from the array.

For example,
Given nums = [0, 1, 3] return 2.

Note:
Your algorithm should run in linear runtime complexity.
Could you implement it using only constant extra space complexity?
'''

class Solution(object):
    def find_missing_number(self, nums):
        if nums is None or len(nums) == 0:
            return None
        n = len(nums)
        sum1 = sum([i for i in xrange(n+1)])
        sum2 = sum(nums)
        return sum1-sum2