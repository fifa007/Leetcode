#!/usr/bin/env python2.7

'''
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
The algorithm should run in linear time and in O(1) space.
Hint:

How many majority elements could it possibly have?
'''

import math

class Solution(object):
    def majority_elem(self, nums):
        if nums is None or len(nums) == 0:
            return []
        n = len(nums)
        can1, c1 = 0, 0
        can2, c2 = 0, 0
        for i in nums:
            if i == can1:
                c1 += 1
            elif i == can2:
                c2 += 1
            elif c1 == 0:
                can1 = i
                c1 = 1
            elif c2 == 0:
                can2 = i
                c2 = 1
            else:
                c1 -= 1
                c2 -= 1
        c1, c2 = 0, 0
        for i in nums:
            if i == can1:
                c1 += 1
            elif i == can2:
                c2 += 1
        if c1 > math.floor(n / 3) and c2 > math.floor(n / 3):
            return [can1, can2]
        elif c1 > math.floor(n / 3):
            return [can1]
        elif c2 > math.floor(n / 3):
            return [can2]
        else:
            return []