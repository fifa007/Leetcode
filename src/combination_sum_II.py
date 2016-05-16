#!/usr/bin/env python2.7


'''
Given a collection of candidate numbers (C) and a target number (T),
find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combinations.
For example, given candidate set 10,1,2,7,6,1,5 and target 8,
A solution set is:
[1, 7]
[1, 2, 5]
[2, 6]
[1, 1, 6]
'''

class Solution(object):
    def helper(self, candidates, target, idx, sum, solution, ret):
        if sum > target:
            return
        if sum == target:
            ret.append(solution)
            return
        for i in xrange(idx, len(candidates)):
            if i > idx and candidates[i] == candidates[i-1]:
                continue
            if candidates[i] <= target:
                sum += candidates[i]
                tmp = solution[:]
                tmp.append(candidates[i])
                self.helper(candidates, target, i+1, sum, tmp, ret)
                sum -= candidates[i]

    def get_combination(self, candidates, target):
        ret = []
        if candidates is None or len(candidates) == 0:
            return ret
        solution = []
        candidates.sort()
        self.helper(candidates, target, 0, 0, solution, ret)
        return ret
