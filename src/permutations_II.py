#!/usr/bin/env python2.7

'''
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[1,1,2], [1,2,1], and [2,1,1].
'''

class Solution(object):
    def helper(self, nums, used, member, ret):
        n = len(nums)
        if len(member) >= n:
            ret.append(member)
            return
        for i in xrange(n):
            if used[i]:
                continue
            if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                continue
            tmp = member[:]
            tmp.append(nums[i])
            used[i] = True
            self.helper(nums, used, tmp, ret)
            used[i] = False

    def unique_permutation(self, nums):
        if nums is None or len(nums) == 0:
            return []
        ret = []
        member = []
        used = [False] * len(nums)
        nums.sort()
        self.helper(nums, used, member, ret)
        return ret