#!/usr/bin/env python2.7


'''
Given an array of n integers where n > 1, nums, return an array output such that output[i]
is equal to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].

Follow up:
Could you solve it with constant space complexity?
(Note: The output array does not count as extra space for the purpose of space complexity analysis.)
'''


class Solution(object):
    def product_except_self(self, nums):
        if nums is None or len(nums) == 0:
            return []
        p = 1
        ret = []
        for i in xrange(len(nums)):
            ret.append(p)
            p *= nums[i]
        i = len(nums) - 1
        p = 1
        while i >= 0:
            ret[i] *= p
            p *= nums[i]
            i -= 1
        return ret