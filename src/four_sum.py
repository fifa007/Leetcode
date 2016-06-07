#!/usr/bin/env python2.7


'''
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target?
Find all unique quadruplets in the array which gives the sum of target.

Note: The solution set must not contain duplicate quadruplets.

For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
'''


class Solution(object):
    def four_sum(self, nums, target):
        if nums is None:
            return []
        n = len(nums)
        nums.sort()
        ret = []
        for i in xrange(n-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in xrange(i+1, n-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                k = j + 1
                l = n - 1
                while k < l:
                    sum = nums[k] + nums[l]
                    val = target - nums[i] - nums[j]
                    if sum == val:
                        ret.append([nums[i], nums[j], nums[k], nums[l]])
                        k += 1
                        l -= 1
                        while k < l and nums[k] == nums[k-1]:
                            k += 1
                        while k < l and nums[l] == nums[l+1]:
                            l -= 1
                    elif sum < val:
                        k += 1
                    else:
                        l -= 1
        return ret
