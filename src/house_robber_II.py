#!/usr/bin/env python2.7


'''
Note: This is an extension of House Robber.

After robbing those houses on that street, the thief has found himself
a new place for his thievery so that he will not get too much attention.
This time, all houses at this place are arranged in a circle.
That means the first house is the neighbor of the last one.
Meanwhile, the security system for these houses remain the same as for those in the previous street.

Given a list of non-negative integers representing the amount of money of each house,
determine the maximum amount of money you can rob tonight without alerting the police.
'''


class Solution(object):
    def helper(self, nums):
        if nums is None or len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        i = 1
        even = 0
        odd = nums[0]
        ret = 0
        while i < len(nums):
            ret = max(even + nums[i], odd)
            even = odd
            odd = ret
            i += 1
        return ret

    def rob(self, nums):
        if nums is None or len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        return max(self.helper(nums[1:]), self.helper(nums[:-1]))