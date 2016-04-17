#!/usr/bin/env python2.7


'''
unit test for word pattern
'''


import unittest
import src.word_pattern


class word_pattern_test(unittest.TestCase):
    sol = src.word_pattern.Solution()

    def test1(self):
        self.failUnless(self.sol.word_patter('abba', 'dog cat cat dog') is True)

    def test2(self):
        self.failUnless(self.sol.word_patter('abda', 'dog cat cat dog') is False)

    def test3(self):
        self.failUnless(self.sol.word_patter('abab', 'foo bar foo dog') is False)