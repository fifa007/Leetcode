#!/usr/bin/env python2.7


'''
unit tests for atoi
'''


import unittest
import src.atoi


class atoi_test(unittest.TestCase):
    sol = src.atoi.Solution()

    def test1(self):
        self.failUnless(self.sol.convert_str_to_int('1234') == 1234)

    def test2(self):
        self.failUnless(self.sol.convert_str_to_int('-1234') == -1234)

    def test3(self):
        self.failUnless(self.sol.convert_str_to_int('12345678999') == src.atoi.INT32_MAX)

    def test4(self):
        self.failUnless(self.sol.convert_str_to_int("") == 0)

    def test5(self):
        self.failUnless(self.sol.convert_str_to_int("2147483648") == 2147483647)

    def test6(self):
        self.failUnless(self.sol.convert_str_to_int("-2147483648") == -2147483648)
