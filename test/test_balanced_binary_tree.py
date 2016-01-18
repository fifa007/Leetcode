#!/usr/bin/env python2.7

'''
unit test for balanced binary tree
'''

import src.balanced_binary_tree
import unittest
import src.data_structure


class balanced_tree_test(unittest.TestCase):
    sol = src.balanced_binary_tree.Solution()

    #
    def test_with_null_root(self):
        self.failUnless(self.sol.is_balanced_binary_tree(None) is not None)

    #
    def test_with_root_only(self):
        binary_tree = src.data_structure.binary_tree()
        binary_tree.add_node(5)
        self.failUnless(self.sol.is_balanced_binary_tree(binary_tree.get_root()) is True)

    def test_tree_not_balanced(self):
        binary_tree = src.data_structure.binary_tree()
        binary_tree.add_node(5)
        binary_tree.add_node(3)
        binary_tree.add_node(8)
        binary_tree.add_node(9)
        binary_tree.add_node(10)
        self.failUnless(self.sol.is_balanced_binary_tree(binary_tree.get_root()) is False)