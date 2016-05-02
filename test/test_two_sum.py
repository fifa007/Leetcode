#!/usr/bin/env python2.7


'''
unit test for two sum
'''

import unittest
import src.two_sum


class two_sum_test(unittest.TestCase):
    sol = src.two_sum.Solution()

    def test1(self):
        nums = [2, 7, 11, 15]
        target = 9
        self.failUnless(self.sol.two_sum(nums, target) == [0, 1])