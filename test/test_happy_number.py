#!/usr/bin/env python2.7


'''
unit test for happy number
'''


import src.happy_number
import unittest


class happy_number_test(unittest.TestCase):
    sol = src.happy_number.Solution()

    #
    def test_with_negative_number(self):
        self.failUnless(self.sol.is_happy_number(-1) == False)

    #
    def test_with_19(self):
        self.failUnless(self.sol.is_happy_number(19) == True)

    #
    def test_with_4(self):
        self.failUnless(self.sol.is_happy_number(4) == False)


def main():
    unittest.main()

if __name__ == "__main__":
    main()