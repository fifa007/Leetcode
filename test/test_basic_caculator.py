#!/usr/bin/env python2.7


'''
unit test for basic caculator
'''

import unittest
import src.basic_calculator

class basic_calculator_test(unittest.TestCase):
    sol = src.basic_calculator.Solution()

    def test1(self):
        actual = self.sol.caculate('2147483647')
        self.failUnless(actual == 2147483647)

    def test2(self):
        actual = self.sol.caculate('1-(5)')
        self.failUnless(actual == -4)