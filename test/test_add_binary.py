#!/usr/bin/env python2.7

'''
unit test for add binary
'''


import unittest
import src.add_binary


class add_binary_test(unittest.TestCase):
    sol = src.add_binary.Solution()

    def test1(self):
        self.failUnless(self.sol.add_binary("1", "1") == "10")

    def test2(self):
        self.failUnless(self.sol.add_binary("10", "1") == "11")