#!/usr/bin/env python2.7


'''
You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed,
the only constraint stopping you from robbing each of them is that
adjacent houses have security system connected and it will automatically contact
the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house,
determine the maximum amount of money you can rob tonight without alerting the police.
'''

import math

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0
        a_0 = 0
        a_1 = nums[0]
        ret = nums[0]
        i = 1
        while i < len(nums):
            ret = max(a_0 + nums[i], a_1)
            a_0 = a_1
            a_1 = ret
            i += 1
        return ret