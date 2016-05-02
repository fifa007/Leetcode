#!/usr/bin/env python2.7

'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''


class Solution(object):
    def two_sum(self, nums, target):
        if nums is None or len(nums) == 0:
            return []
        key_val = dict()
        for i in xrange(len(nums)):
            if nums[i] in key_val:
                return [key_val[nums[i]], i]
            key_val[target - nums[i]] = i
        return []
