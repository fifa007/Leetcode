#!/usr/bin/env python2.7


'''
unit test for count primes
'''

import unittest
import src.count_primes


class count_primes_test(unittest.TestCase):
    sol = src.count_primes.Solution()

    def test1(self):
        self.failUnless(self.sol.count_primes(4) == 2)