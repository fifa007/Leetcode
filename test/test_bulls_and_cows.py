#!/usr/bin/env python2.7

'''
unit test for bulls and cows
'''

import unittest
import src.bulls_and_cows


class bulls_and_cows_test(unittest.TestCase):
    sol = src.bulls_and_cows.Solution()

    def test1(self):
        self.failUnless(self.sol.get_hints('1807', '7810') == '1A3B')

    def test2(self):
        self.failUnless(self.sol.get_hints('1123', '0111') == '1A1B')

    def test3(self):
        self.failUnless(self.sol.get_hints('1122', '2211') == '0A4B')

def main():
    unittest.main()

if __name__ == "__main__":
    main()