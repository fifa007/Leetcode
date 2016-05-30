#!/usr/bin/env python2.7


'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.
'''


class Solution(object):
    def can_reach(self, nums):
        if nums is None or len(nums) == 1:
            return True
        n = len(nums)
        max_steps = 0
        for i in xrange(n):
            if i > max_steps or max_steps >= n-1:
                break
            max_steps = max(max_steps, i + nums[i])
        return True if max_steps >= n-1 else False