#!/usr/bin/env python2.7


'''
unit test for ugly_number
'''

import src.ugly_number
import unittest


class ugly_number_test(unittest.TestCase):
    sol = src.ugly_number.Solution()

    #
    def test_with_n_equals_zero(self):
        self.failUnless(self.sol.is_ugly(0) == False)

    #
    def test_with_n_equals_one(self):
        self.failUnless(self.sol.is_ugly(1) == True)

    #
    def test_with_n_equals_six(self):
        self.failUnless(self.sol.is_ugly(6) == True)

    #
    def test_with_n_equals_123456789(self):
        self.failUnless(self.sol.is_ugly(123456789) == False)

    #
    def test_with_n_equals_14(self):
        self.failUnless(self.sol.is_ugly(14) == False)