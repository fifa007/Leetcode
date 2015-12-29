#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

'''
unit test for valid anagram
'''

import unittest
import src.valid_anagram

class valid_anagram_test(unittest.TestCase):

    sol = src.valid_anagram.Solution()

    #null string
    def test_null_string(self):
        self.failUnless(self.sol.is_valid_anagram(None, None))

    #string with unequal length
    def test_strings_with_different_length(self):
        self.failUnless(self.sol.is_valid_anagram("ab", "a") == False)

    #string with common length
    def test_strings_with_same_length(self):
        self.failUnless(self.sol.is_valid_anagram("anagram", "nagaram"))

    #string containing unicode
    def test_string_containing_unicode(self):
        s1 = '債務の天井'.decode('utf-8')
        s2 = '債務天井の'.decode('utf-8')
        self.failUnless(self.sol.is_valid_anagram(s1, s2))

def main():
    unittest.main()


if __name__ == "__main__":
    main()