#!/usr/bin/env python2.7


'''
unit test for palindrome number
'''

import unittest
import src.palindrom_number
import sys

class palindrome_number_test(unittest.TestCase):
    sol = src.palindrom_number.Solution()

    def test_with_negative_2147483648(self):
        self.failUnless(self.sol.is_palindrom_number(-2147483648) == False)

    def test_with_121(self):
        self.failUnless(self.sol.is_palindrom_number(121) == True)

    def test_with_minimum(self):
        self.failUnless(self.sol.is_palindrom_number(-sys.maxint-1) == False)