#!/usr/bin/env python2.7

import unittest
import src.add_digits


class add_digits_test(unittest.TestCase):
    sol = src.add_digits.Solution()

    #input = 0
    def test_with_zero(self):
        self.failUnless(self.sol.add_digits(0) == 0)

    #input % 9 == 0
    def test_with_num_dividable_by_nine(self):
        self.failUnless(self.sol.add_digits(9) == 9)

    #input % 9 != 0
    def test_with_num_not_dividable_by_nine(self):
        self.failUnless(self.sol.add_digits(12) == 3)

def main():
    unittest.main()


if __name__ == "__main__":
    main()