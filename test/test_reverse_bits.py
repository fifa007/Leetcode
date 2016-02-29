#!/usr/bin/env python2.7


'''
unit test for reverse bits
'''

import unittest
import src.reverse_bits

class reverse_bits_test(unittest.TestCase):
    sol = src.reverse_bits.Solution()

    def test_reverse_bits(self):
        n = 43261596
        self.failUnless(self.sol.reverse_bits(n) == 964176192)

