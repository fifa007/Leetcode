#!/usr/bin/env python2.7


'''
Given a sorted integer array without duplicates, return the summary of its ranges.

For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].
'''


class Solution(object):
    def summary_range(self, nums):
        if nums is None or len(nums) == 0:
            return []
        n = len(nums)
        i = 0
        j = 1
        ret = []
        while j < n:
            while j < n and nums[j] == nums[j-1] + 1:
                j += 1
            ret.append(self.build_range(nums, i, j))
            i = j
            j += 1
        ret.append(self.build_range(nums, i, j))
        return ret

    def build_range(self, nums, i, j):
        if i == j-1:
            return str(nums[i])
        else:
            return str(nums[i]) + '->' + str(nums[j-1])