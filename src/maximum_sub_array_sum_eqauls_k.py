#!/usr/bin/env python2.7


'''
Given an array nums and a target value k, find the maximum length of a subarray that sums to k.
If there isn't one, return 0 instead.

Example 1:
Given nums = [1, -1, 5, -2, 3], k = 3,
return 4. (because the subarray [1, -1, 5, -2] sums to 3 and is the longest)

Example 2:
Given nums = [-2, -1, 2, 1], k = 1,
return 2. (because the subarray [-1, 2] sums to 1 and is the longest)

Follow Up:
Can you do it in O(n) time?
'''


class Solution(object):
    def max_subarray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if nums is None:
            return 0
        v = 0
        sum_list = []
        for num in nums:
            v += num
            sum_list.append(v)
        dict = {}
        ret = 0
        for idx, sum in enumerate(sum_list):
            if sum == k:
               ret = max(ret, idx + 1)
            if dict.has_key(sum):
                ret = max(ret, abs(dict[sum] - idx))
            else:
                if dict.has_key(sum + k) == False:
                    dict[sum + k] = idx
        return ret