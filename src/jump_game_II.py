#!/usr/bin/env python2.7

'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

For example:
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1,
then 3 steps to the last index.)
'''


class Solution(object):
    def jump(self, nums):
        if nums is None or len(nums) == 0:
            return 0
        n = len(nums)
        ret = 0
        curr = 0
        last = 0
        for i in xrange(n):
            if i > last:
                last = curr
                ret += 1
            curr = max(curr, i + nums[i])
        return ret