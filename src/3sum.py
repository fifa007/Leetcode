#!/usr/bin/env python2.7


'''
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''


class Solution(object):
    def three_sum(self, nums):
        if nums is None or len(nums) < 3:
            return []
        ret = []
        n = len(nums)
        nums.sort()
        for i in xrange(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j, k = i+1, n-1
            while j < k:
                val = nums[i] + nums[j] + nums[k]
                if val == 0:
                    ret.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
                elif val < 0:
                    j += 1
                else:
                    k -= 1
        return ret