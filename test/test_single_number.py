#!/usr/bin/env python2.7


'''
unit test for single number
'''

import unittest
import src.single_number


class single_number_test(unittest.TestCase):
    sol = src.single_number.Solution()

    def test1(self):
        nums = [1, 1, 2]
        self.failUnless(self.sol.single_number(nums) == 2)

    def test2(self):
        nums = [1, 1]
        self.failUnless(self.sol.single_number(nums) == 0)