#!/usr/bin/env python2.7


'''
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].
'''


class Solution(object):
    def rotate(self, nums, k):
        if nums is None or len(nums) == 0:
            return
        if k % len(nums) == 0:
            return
        r = k % len(nums)
        nums[0:0] = nums[-r:]
        del nums[-r:]