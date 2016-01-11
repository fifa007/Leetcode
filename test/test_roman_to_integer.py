#!/usr/bin/env python2.7

'''
unit test for roman_to_integer
'''


import unittest
import src.roman_to_integer


class test_roman_to_integer(unittest.TestCase):
    sol = src.roman_to_integer.Soluttion()

    #
    def test_with_X(self):
        self.failUnless(self.sol.roman_to_integer('X') == 10)

    #
    def test_with_XC(self):
        self.failUnless(self.sol.roman_to_integer('XC') == 90)

    #
    def test_with_MCMLIV(self):
        self.failUnless(self.sol.roman_to_integer('MCMLIV') == 1954)


def main():
    unittest.main()


if __name__ == "__main__":
    main()