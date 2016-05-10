#!/usr/bin/env python2.7


'''
Given a sorted array and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0
'''


class Solution(object):
    def search_helper(self, nums, target, start, end):
        if start > end:
            return start
        if start == end:
            return start if target <= nums[start] else start+1
        mid = start + (end - start) / 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return self.search_helper(nums, target, mid+1, end)
        else:
            return self.search_helper(nums, target, start, mid-1)

    def search_insert_pos(self, nums, target):
        return self.search_helper(nums, target, 0, len(nums)-1)