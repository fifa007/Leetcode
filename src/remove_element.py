#!/usr/bin/env python2.7

'''
Given an array and a value, remove all instances of that value in place and return the new length.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.
'''


class Solution(object):
    def remove_element(self, nums, value):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if nums is None:
            return 0
        l = len(nums)
        i = 0
        j = l - 1
        while i <= j:
            if nums[i] != value:
                i += 1
                continue
            if nums[j] == value:
                j -= 1
                continue
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        return i