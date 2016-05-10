#!/usr/bin/env python2.7


'''
unit test for unique bst
'''


import unittest
import src.unique_binary_search_tree

class unique_bst_test(unittest.TestCase):
    sol = src.unique_binary_search_tree.Solution()

    def test1(self):
        self.failUnless(self.sol.unique_tree(2) == 2)

    def test2(self):
        self.failUnless(self.sol.unique_tree(3) == 5)