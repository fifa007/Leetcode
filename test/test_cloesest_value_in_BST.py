#!/usr/bin/env python2.7

'''
unit test for closest BST value
'''

import src.closest_binary_search_tree_value
import src.data_structure
import unittest

class closest_bst_value_test(unittest.TestCase):
    sol = src.closest_binary_search_tree_value.Solution()

    #
    def test_with_null_tree(self):
        self.failUnless(self.sol.find_closest_value_in_BST(None, 2.5) is None)

    #
    def test_with_root_value_is_target(self):
        bst = src.data_structure.binary_tree()
        bst.add_node(5)
        bst.add_node(3)
        bst.add_node(8)
        self.failUnless(self.sol.find_closest_value_in_BST(bst.get_root(), 5) == 5)

    #
    def test_with_target_less_than_root_value(self):
        bst = src.data_structure.binary_tree()
        bst.add_node(12)
        bst.add_node(8)
        bst.add_node(5)
        bst.add_node(11)
        bst.add_node(16)
        self.failUnless(self.sol.find_closest_value_in_BST(bst.get_root(), 11.4) == 11)

    #
    def test_with_single_root_tree(self):
        bst = src.data_structure.binary_tree()
        bst.add_node(8)
        self.failUnless(self.sol.find_closest_value_in_BST(bst.get_root(), 13.1) == 8)

    #
    def test_with_target_on_right_side_of_root(self):
        bst = src.data_structure.binary_tree()
        bst.add_node(12)
        bst.add_node(8)
        bst.add_node(5)
        bst.add_node(11)
        bst.add_node(16)
        self.failUnless(self.sol.find_closest_value_in_BST(bst.get_root(), 15.5) == 16)
