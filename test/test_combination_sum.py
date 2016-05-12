#!/usr/bin/env python2.7


'''
unit test for combination sum
'''


import unittest
import src.combination_sum

class combination_sum_test(unittest.TestCase):
    sol = src.combination_sum.Solution()

    def test1(self):
        candidates = [1]
        target = 1
        self.failUnless(self.sol.get_combination_sum(candidates, target) == [[1]])

    def test2(self):
        candidates = [1, 2]
        target = 2
        self.failUnless(self.sol.get_combination_sum(candidates, target) == [[1,1],[2]])