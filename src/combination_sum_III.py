#!/usr/bin/env python2.7


'''
Find all possible combinations of k numbers that add up to a number n,
given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Ensure that numbers within the set are sorted in ascending order.


Example 1:

Input: k = 3, n = 7

Output:

[[1,2,4]]

Example 2:

Input: k = 3, n = 9

Output:

[[1,2,6], [1,3,5], [2,3,4]]

'''


class Solution(object):
    def helper(self, nums, target, k, idx, sum, sol, ret):
        if sum > target or len(sol) > k:
            return
        if sum == target:
            if len(sol) == k:
                ret.append(sol)
                return
            else:
                return
        for i in xrange(idx, len(nums)):
            if nums[i] > 9:
                continue
            if nums[i] <= target:
                sum += nums[i]
                tmp = sol[:]
                tmp.append(nums[i])
                self.helper(nums, target, k, i+1, sum, tmp, ret)
    def get_combinations(self, k, n):
        ret = []
        sol = []
        nums = [i+1 for i in xrange(n)]
        self.helper(nums, n, k, 0, 0, sol, ret)
        return ret