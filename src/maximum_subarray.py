#!/usr/bin/env python2.7


'''
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
the contiguous subarray [4,−1,2,1] has the largest sum = 6.

'''

from sys import maxint

class Solution(object):
    def max_sub_array(self, nums):
        if nums is None or len(nums) == 0:
            return 0
        ret = -maxint - 2
        sum = -maxint - 2
        for num in nums:
            sum = max(sum + num, num)
            ret = max(ret, sum)
        return ret