#!/usr/bin/env python2.7

'''
Given a string of numbers and operators, return all possible results
from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.


Example 1
Input: "2-1-1".

((2-1)-1) = 0
(2-(1-1)) = 2
Output: [0, 2]


Example 2
Input: "2*3-4*5"

(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10
Output: [-34, -14, -10, -10, 10]
'''


class Solution(object):
    def compute(self, a, b, op):
        if op == '+':
            return a + b
        if op == '-':
            return a - b
        if op == '*':
            return a * b

    def generate_key(self, start, end):
        return str(start) + '-' + str(end)

    def helper(self, input, start, end, memo):
        key = self.generate_key(start, end)
        if memo.has_key(key):
            return memo[key]
        memo[key] = []
        n = 0
        i = start
        while i <= end:
            if input[i].isdigit():
                n = n * 10 + int(input[i])
                i += 1
            else:
                break
        if i == end + 1:
            memo[key] = [n]
            return memo[key]
        for i in xrange(start, end):
            if input[i].isdigit():
                continue
            lefts = self.helper(input, start, i-1, memo)
            rights = self.helper(input, i+1, end, memo)
            for j in xrange(len(lefts)):
                for k in xrange(len(rights)):
                    memo[key].append(self.compute(lefts[j], rights[k], input[i]))
        return memo[key]

    def diff_ways_to_compute(self, input):
        memo = dict()
        return self.helper(input, 0, len(input)-1, memo)