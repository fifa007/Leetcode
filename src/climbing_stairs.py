#!/usr/bin/env python2.7


'''
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''


class Solution(object):
    def climbing_stairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        if n <= 2:
            return n
        step_1 = 2
        step_2 = 1
        steps = 0
        for num in range(3, n + 1):
            steps = step_1 + step_2
            step_2 = step_1
            step_1 = steps
        return steps