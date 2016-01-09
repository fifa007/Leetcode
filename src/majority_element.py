#!/usr/bin/env python2.7

'''
Given an array of size n, find the majority element. The majority element is the element that appears more than n/2
times, You may assume that the array is non-empty and the majority element always exist in the array.
'''


class Solution(object):
    def majority_element(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        for num in nums:
            if dict.has_key(num):
                dict[num] += 1
            else:
                dict[num] = 1
            if dict.get(num) > len(nums) / 2:
                return num
        return 0