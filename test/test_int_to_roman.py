#!/usr/bin/env python2.7


'''
unit test for int to roman
'''

import unittest
import src.int_to_roman

class int_to_roman_test(unittest.TestCase):
    sol = src.int_to_roman.Solution()

    def test1(self):
        self.failUnless(self.sol.int_to_roman(1954) == 'MCMLIV')