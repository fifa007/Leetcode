#!/usr/bin/env python2.7


'''
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target.
Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

'''


class Solution(object):
    def three_sum_closest(self, nums, target):
        ret = 0
        N = len(nums)
        nums.sort()
        dist = float('inf')
        for k in xrange(N-1):
            i = k + 1
            j = N - 1
            while i < j:
                s = nums[i] + nums[j] + nums[k]
                if s == target:
                    return s
                elif s < target:
                    d = target - s
                    if d < dist:
                        dist = d
                        ret = s
                    i += 1
                else:
                    d = s - target
                    if d < dist:
                        dist = d
                        ret = s
                    j -= 1
        return ret
