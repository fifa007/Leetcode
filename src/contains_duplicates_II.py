#!/usr/bin/env python2.7


'''
Given an array of integers and an integer k, find out whether there are two distinct
indices i and j in the array such that nums[i] = nums[j] and the difference between i and j is at most k.
'''

class Solution(object):
    def contains_nearby_duplicates(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if nums is None:
            return False
        dict = {}
        for i in range(len(nums)):
            if dict.has_key(nums[i]) and (i - dict[nums[i]]) <= k:
                return True
            else:
                dict[nums[i]] = i
        return False