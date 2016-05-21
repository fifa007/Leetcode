#!/usr/bin/env python2.7

'''
A peak element is an element that is greater than its neighbors.

Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that num[-1] = num[n] = -∞.

For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.
'''


class Solution(object):
    def find_peak_elem_1(self, nums):
        if nums is None or len(nums) == 0:
            return -1
        if len(nums) == 1:
            return 0
        n = len(nums)
        i = 0
        while i < n:
            if i > 0 and i < n-1:
                if nums[i] > nums[i-1] and nums[i] < nums[i+1]:
                    return i
            elif i == 0:
                if nums[i] > nums[i+1]:
                    return 0
            else:
                if nums[i] > nums[i-1]:
                    return n-1
        return -1

    def find_peak_elem_2(self, nums):
        if nums is None or len(nums) == 0:
            return -1
        if len(nums) == 1:
            return 0
        n = len(nums)
        start = 0
        end = n - 1
        while start <= end:
            mid = start + (end - start)/2
            if (mid == 0 or nums[mid] > nums[mid-1]) and \
                    (mid == n-1 or nums[mid] > nums[mid+1]):
                return mid
            elif mid > 0 and nums[mid-1] > nums[mid]:
                end = mid-1
            else:
                start = mid + 1
        return -1