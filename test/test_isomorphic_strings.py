#!/usr/bin/env python2.7

'''
unit test for isomorphic_strings
'''

import src.isomorphic_strings
import unittest


class isomorphic_strings_test(unittest.TestCase):
    sol = src.isomorphic_strings.Solution()

    def test1(self):
        self.failUnless(self.sol.is_isomorphic_strings('egg', 'add') == True)

    def test2(self):
        self.failUnless(self.sol.is_isomorphic_strings('abc', 'ab') == False)

    def test3(self):
        self.failUnless(self.sol.is_isomorphic_strings(None, None) == True)

    def test4(self):
        self.failUnless(self.sol.is_isomorphic_strings(None, 'a') == False)

    def test5(self):
        self.failUnless(self.sol.is_isomorphic_strings('foo', 'bar') == False)

    def test6(self):
        self.failUnless(self.sol.is_isomorphic_strings('paper', 'title') == True)

    def test7(self):
        self.failUnless(self.sol.is_isomorphic_strings('ab', 'aa') == False)