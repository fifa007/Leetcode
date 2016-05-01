#!/usr/bin/env python2.7

'''
unit test for reverse integer
'''


import unittest
import src.reverse_integer

class reverse_integer_test(unittest.TestCase):
    sol = src.reverse_integer.Solution()

    def test1(self):
        self.failUnless(self.sol.reverse_integer(123) == 321)

    def test2(self):
        self.failUnless(self.sol.reverse_integer(-123) == -321)

    def test3(self):
        self.failUnless(self.sol.reverse_integer(1234567899) == 0)

def main():
    unittest.main()

if __name__ == "__main__":
    main()