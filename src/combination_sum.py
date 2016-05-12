#!/usr/bin/env python2.7

'''
combination sum
'''


class Solution(object):
    def helper(self, candidates, target, idx, sum, solution, ret):
        if target < sum or idx == len(candidates):
            return
        if target == sum:
            ret.append(solution)
            return
        for i in xrange(idx, len(candidates)):
            sum += candidates[i]
            tmp = solution[:]
            tmp.append(candidates[i])
            self.helper(candidates, target, i, sum, tmp, ret)
            sum -= candidates[i]

    def get_combination_sum(self, candidates, target):
        ret = []
        solution = []
        sum = 0
        self.helper(candidates, target, 0, 0, solution, ret)
        return ret