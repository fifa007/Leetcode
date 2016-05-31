#!/usr/bin/env python2.7

'''
Given an array of n positive integers and a positive integer s, find the minimal length of a subarray of which the sum ≥ s. If there isn't one, return 0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.

click to show more practice.

More practice:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).
'''


class Solution(object):
    def min_size_sub_array(self, nums, s):
        if nums is None or len(nums) == 0 or s < 0:
            return 0
        n = len(nums)
        left, right, sum = 0, 0, 0
        ret = n + 1
        while right < n:
            while right < n and sum < s:
                sum += nums[right]
                right += 1
            while left < right and sum >= s:
                ret = min(ret, right-left)
                sum -= nums[left]
                left += 1

        return [0, ret][right <= n]