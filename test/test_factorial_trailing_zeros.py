#!/usr/bin/env python2.7


'''
unit tests for factorial trailing zeros
'''


import unittest
import src.factorial_trailing_zeros


class factorial_trailing_zeros_test(unittest.TestCase):
    sol = src.factorial_trailing_zeros.Solution()

    def test_with_zero(self):
        self.failUnless(self.sol.count_factorial_trailing_zeros(0) == 0)

    def test_with_7(self):
        self.failUnless(self.sol.count_factorial_trailing_zeros(7) == 1)

    def test_with_21(self):
        self.failUnless(self.sol.count_factorial_trailing_zeros(21) == 4)

    def test_with_28(self):
        self.failUnless(self.sol.count_factorial_trailing_zeros(28) == 6)

def main():
    unittest.main()

if __name__ == "__main__":
    main()