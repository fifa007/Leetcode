#!/usr/bin/env python2.7

'''
unit test for house robber
'''

import unittest
import src.house_robber


class house_robber_test(unittest.TestCase):
    sol = src.house_robber.Solution()

    #
    def test_with_empty_houses(self):
        self.failUnless(self.sol.rob(None) == 0)
        self.failUnless(self.sol.rob([]) == 0)

    #
    def test_with_one_house(self):
        houses = [3]
        self.failUnless(self.sol.rob(houses) == 3)

    #
    def test_with_houses(self):
        houses = [5, 2, 3, 8]
        self.failUnless(self.sol.rob(houses) == 13)