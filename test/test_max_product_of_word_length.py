#!/usr/bin/env python2.7


'''
unit tests for max product of word length
'''


import unittest
import src.max_product_of_word_length


class max_product_of_word_length_test(unittest.TestCase):
    sol = src.max_product_of_word_length.Solution()

    def test1(self):
        words = ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
        self.failUnless(self.sol.max_product(words) == 16)


    def test2(self):
        words = ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
        self.failUnless(self.sol.max_product(words) == 4)

    def test3(self):
        words = ["a", "aa", "aaa", "aaaa"]
        self.failUnless(self.sol.max_product(words) == 0)