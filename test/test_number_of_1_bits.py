#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

'''
unit test of number_of_1_bits
'''

import unittest
import src.number_of_1_bits


class number_of_1_bits_test(unittest.TestCase):
    sol = src.number_of_1_bits.Solution()

    #n = 0
    def test_with_zero(self):
        self.failUnless(self.sol.number_of_1_bits(0) == 0)

    #n = 11
    def test_with_11(self):
        self.failUnless(self.sol.number_of_1_bits(11) == 3)

def main():
    unittest.main()


if __name__ == "__main__":
    main()