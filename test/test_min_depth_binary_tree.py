#!/usr/bin/env python2.7


'''
unit tests for min_depth_binary_tree
'''

import unittest
import src.minimum_depth_binary_tree
import src.data_structure

class min_depth_binary_tree_test(unittest.TestCase):
    sol = src.minimum_depth_binary_tree.Solution()

    def test_with_null_root(self):
        self.failUnless(self.sol.min_depth(None) == 0)

    def test_with_left_tree_ONLY(self):
        binary_tree = src.data_structure.binary_search_tree()
        binary_tree.add_node(8)
        binary_tree.add_node(5)
        binary_tree.add_node(3)
        binary_tree.add_node(6)
        self.failUnless(self.sol.min_depth(binary_tree.get_root()) == 3)

    def test_with_binary_tree(self):
        binary_tree = src.data_structure.binary_search_tree()
        binary_tree.add_node(8)
        binary_tree.add_node(5)
        binary_tree.add_node(10)
        binary_tree.add_node(6)
        self.failUnless(self.sol.min_depth(binary_tree.get_root()) == 2)