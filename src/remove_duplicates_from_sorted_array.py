#!/usr/bin/env python2.7

'''
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the new length.
'''


class Solution(object):
    def remove_duplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0
        i = 0
        j = 1
        while j < len(nums):
            if nums[i] != nums[j]:
                nums[i + 1], nums[j] = nums[j], nums[i + 1]
                i += 1
            j += 1
        return i + 1