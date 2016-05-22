#!/usr/bin/env python2.7


'''
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.
'''

class Solution(object):
    def helper(self, nums, start, end, target):
        if start > end:
            return -1
        mid = start + (end-start)/2
        if nums[mid] == target:
            return mid
        if nums[mid] > nums[start]:
            if target >= nums[start] and target < nums[mid]:
                return self.helper(nums, start, mid-1, target)
            else:
                return self.helper(nums, mid+1, end, target)
        elif nums[mid] < nums[start]:
            if target > nums[mid] and target <= nums[end]:
                return self.helper(nums, mid+1, end, target)
            else:
                return self.helper(nums, start, mid-1, target)
        else:
            if nums[mid] != nums[end]:
                return self.helper(nums, mid+1, end, target)
            else:
                v = self.helper(nums, start, mid-1, target)
                if v == -1:
                    return self.helper(nums, mid+1, end, target)
                return v

    def search_in_rotated_array(self, nums, target):
        if nums is None:
            return -1
        return self.helper(nums, 0, len(nums)-1, target)