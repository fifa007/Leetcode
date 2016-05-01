#!/usr/bin/env python2.7


'''
unit test for zig_zag conversion
'''


import unittest
import src.zig_zag_conversion

class zig_zag_conversion_test(unittest.TestCase):
    sol = src.zig_zag_conversion.Solution()

    def test1(self):
        self.failUnless(self.sol.conversion("ABCDE", 3) == "AEBDC")