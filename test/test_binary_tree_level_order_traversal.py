#!/usr/bin/env python2.7

'''
unit test for binary_tree_level_order_traversal
'''


import unittest
import src.binary_tree_level_order_traversal
import src.data_structure

class binary_tree_level_order_traversal_test(unittest.TestCase):
    sol = src.binary_tree_level_order_traversal.Solution()

    #
    def test_with_null_tree(self):
        self.failUnless(self.sol.binary_tree_level_order_traversal(None) == [])

    #
    def test_with_single_node_tree(self):
        binary_tree = src.data_structure.binary_search_tree()
        binary_tree.add_node(1)
        self.failUnless(self.sol.binary_tree_level_order_traversal(binary_tree.get_root()) == [[1]])

    def test_with_binary_tree(self):
        binary_tree = src.data_structure.binary_search_tree()
        binary_tree.add_node(5)
        binary_tree.add_node(2)
        binary_tree.add_node(8)
        binary_tree.add_node(1)
        binary_tree.add_node(3)

        expected = [[5], [2, 8], [1, 3]]
        self.failUnless(self.sol.binary_tree_level_order_traversal(binary_tree.get_root()) == expected)