#!/usr/bin/env python2.7

'''
unit test for single number II
'''

import unittest
import src.single_number_II

class single_number_II_test(unittest.TestCase):
    sol = src.single_number_II.Solution()

    def test(self):
        nums = [-1, -1, -1, 1]
        self.failUnless(self.sol.single_number(nums) == 1)

    def test(self):
        nums = [-1, -1, -1, -2]
        self.failUnless(self.sol.single_number(nums) == -2)