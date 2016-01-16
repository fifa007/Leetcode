#!/usr/bin/env python2.7


'''
unit test for power of two
'''


import src.power_of_two
import unittest


class power_of_two_test(unittest.TestCase):
    sol = src.power_of_two.Solution()

    #
    def test_with_zero(self):
        self.failUnless(self.sol.is_power_of_two(0) == False)

    #
    def test_with_one(self):
        self.failUnless(self.sol.is_power_of_two(1) == True)

    #
    def test_with_two(self):
        self.failUnless(self.sol.is_power_of_two(2) == True)

    #
    def test_with_four(self):
        self.failUnless(self.sol.is_power_of_two(4) == True)

    #
    def test_with_three(self):
        self.failUnless(self.sol.is_power_of_two(3) == False)