#!/usr/bin/env python2.7

'''
unit test for super ugly number
'''


import unittest
import src.super_ugly_number


class super_ugly_number_test(unittest.TestCase):
    sol = src.super_ugly_number.Solution()

    def test1(self):
        primes = [2]
        actual = self.sol.super_ugly_number(4, primes)
        self.failUnless(actual == 8)