#!/usr/bin/env python2.7


'''
unit test for sum root to leaf
'''

import unittest
import src.sum_root_to_leaf
import src.data_structure

class sum_root_to_leaf_test(unittest.TestCase):
    sol = src.sum_root_to_leaf.Solution()

    def test1(self):
        root = src.data_structure.tree_node(9)
        actual = self.sol.sum_root_to_leaf(root)
        expected = 9
        self.failUnless(actual == expected)