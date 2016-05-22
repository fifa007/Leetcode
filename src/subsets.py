#!/usr/bin/env python2.7


'''
Given a set of distinct integers, nums, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''


class Solution(object):
    def get_subsets(self, nums):
        if nums is None:
            return None
        ret = [[]]
        nums.sort()
        for num in nums:
            l = len(ret)
            for i in xrange(l):
                tmp = ret[i][:]
                tmp.append(num)
                ret.append(tmp)
        return ret