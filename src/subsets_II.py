#!/usr/bin/env python2.7


'''
Given a collection of integers that might contain duplicates, nums, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If nums = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
'''


class Solution(object):
    def helper(self, nums, idx, sol, ret):
        for i in xrange(idx, len(nums)):
            if i > idx and nums[i] == nums[i-1]:
                continue
            tmp = sol[:]
            tmp.append(nums[i])
            ret.append(tmp)
            self.helper(nums, i+1, tmp, ret)

    def subsets(self, nums):
        if nums is None or len(nums) == 0:
            return None
        sol = []
        ret = [[]]
        nums.sort()
        self.helper(nums, 0, sol, ret)
        return ret