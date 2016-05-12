#!/usr/bin/env python2.7


'''
Given an array of numbers nums, in which exactly two elements appear only once and
all the other elements appear exactly twice. Find the two elements that appear only once.

For example:

Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].

Note:
The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?
'''


class Solution(object):
    def single_number(self, nums):
        if nums is None or len(nums) < 2:
            return []
        xor_1 = 0
        for num in nums:
            xor_1 ^= num
        k = 0
        while k < 32:
            if (xor_1 >> k) & 1 == 1:
                break
            k += 1
        xor_2 = 0
        for num in nums:
            if (num >> k) & 1 == 1:
                xor_2 ^= num
        return [xor_2, xor_1 ^ xor_2]