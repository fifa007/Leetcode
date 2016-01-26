#!/usr/bin/env python2.7


'''
unit test for strobogrammatic number
'''

import unittest
import src.strobogrammatic_number


class strobogrammatic_number_test(unittest.TestCase):
    sol = src.strobogrammatic_number.Solution()

    #
    def test_with_negative_1(self):
        self.failUnless(self.sol.is_strobogrammatic_number('-1') == False)

    #
    def test_with_zero(self):
        self.failUnless(self.sol.is_strobogrammatic_number('0') == True)

    #
    def test_with_88(self):
        self.failUnless(self.sol.is_strobogrammatic_number('88') == True)

    #
    def test_with_333(self):
        self.failUnless(self.sol.is_strobogrammatic_number('33') == False)

    #
    def test_with_69(self):
        self.failUnless(self.sol.is_strobogrammatic_number('69') == True)

    def test_with_96(self):
        self.failUnless(self.sol.is_strobogrammatic_number('96') == True)

    def test_with_966(self):
        self.failUnless(self.sol.is_strobogrammatic_number('966') == False)