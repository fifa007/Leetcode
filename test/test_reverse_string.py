#!/usr/bin/env python2.7

'''
unit test for reverse string
'''


import unittest
import src.reverse_string


class reverse_string_test(unittest.TestCase):
    sol = src.reverse_string.Solution()

    def test1(self):
        self.failUnless(self.sol.reverse_string(None) is None)

    def test2(self):
        self.failUnless(self.sol.reverse_string("hello") == "olleh")

    def test3(self):
        self.failUnless(self.sol.reverse_string("hello world!") == "!dlrow olleh")