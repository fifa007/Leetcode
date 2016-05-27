#!/usr/bin/env python2.7

'''
Given a sorted array of integers, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
'''


class Solution(object):
    def helper(self, nums, target, start, end):
        if start > end:
            return [-1] * 2
        mid = start + (end-start)/2
        if nums[mid] == target:
            l, _ = self.helper(nums, target, start, mid-1)
            low = l if l != -1 else mid
            _, r = self.helper(nums, target, mid+1, end)
            high = r if r != -1 else mid
        elif nums[mid] < target:
            low, high = self.helper(nums, target, mid+1, end)
        else:
            low, high = self.helper(nums, target, start, mid-1)
        return [low, high]

    def search_for_range(self, nums, target):
        return self.helper(nums, target, 0, len(nums)-1)