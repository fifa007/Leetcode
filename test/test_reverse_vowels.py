#!/usr/bin/env python2.7


'''
unit test for reverse vowels in string
'''

import unittest
import src.reverse_vowels_of_a_string

class reverse_vowels_test(unittest.TestCase):
    sol = src.reverse_vowels_of_a_string.Solution()

    def test1(self):
        s = 'hello'
        self.failUnless(self.sol.reverse_vowels(s) == 'holle')

    def test2(self):
        s = 'HellO'
        self.failUnless(self.sol.reverse_vowels(s) == 'HOlle')

