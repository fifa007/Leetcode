#!/usr/bin/env python2.7


'''
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.
'''


class Solution(object):
    def helper(self, nums, start, end):
        if start > end:
            return 0
        if start == end:
            return nums[start]
        mid = start + (end - start)/2
        if nums[mid] > nums[start] and nums[mid] > nums[end]:
            return self.helper(nums, mid, end)
        elif nums[mid] < nums[start] and nums[mid] < nums[end]:
            return self.helper(nums, start, mid)
        else:
            return min(nums[start], nums[end])

    def find(self, nums):
        return self.helper(nums, 0, len(nums)-1)