#!/usr/bin/env python2.7

'''
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

The update(i, val) function modifies nums by updating the element at index i to val.
Example:
Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8
Note:
The array is only modifiable by the update function.
You may assume the number of calls to update and sumRange function is distributed evenly.
'''


class Solution(object):
    def low_bit(self, x):
        return x & ~(x-1)

    def __init__(self, nums):
        if nums is None or len(nums) == 0:
            self.elems = [0]
            self.bit = [0]
            return
        self.elems = [0] + nums
        n = len(self.elems)
        self.bit = [0] * n
        for i in xrange(1, n):
            self.bit[i] = self.elems[i]
            for j in xrange(i-1, 0, -self.low_bit(i)):
                self.bit[i] += self.elems[j]

    def update(self, i, value):
        if self.elems is None or len(self.elems) < 2 or i >= len(self.elems):
            return
        j = i + 1
        delta = value - self.elems[i+1]
        while j < len(self.bit):
            self.bit[j] +=delta
        self.elems[i+1] = value

    def get_sum(self, N):
        ret = 0
        j = N
        while j > 0:
            ret += self.bit[j]
            j -= self.low_bit(j)
        return ret

    def range_sum(self, i, j):
        return self.get_sum(j+1) - self.get_sum(i)