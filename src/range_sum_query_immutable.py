#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-


'''
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
Note:
You may assume that the array does not change.
There are many calls to sumRange function.
'''


class num_array(object):
    def __init__(self, nums):
        if len(nums) == 0:
            return
        self.nums = nums
        self.sums = [nums[0]]
        i = 1
        while i < len(nums):
            self.sums.append(self.sums[i - 1] + self.nums[i])
            i += 1

    def range_sum_query(self, i, j):
        return self.sums[j] - self.sums[i] + self.nums[i]