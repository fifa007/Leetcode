#!/usr/bin/env python2.7


'''
unit test for binary tree level order traversal II
'''

import src.binary_tree_level_order_traversal_II
import src.data_structure
import unittest
import collections
compare = lambda x, y: collections.Counter(x) == collections.Counter(y)


class binary_tree_level_order_traversal_II_test(unittest.TestCase):
    sol = src.binary_tree_level_order_traversal_II.Solution()


    #
    def test_with_null_root(self):
        self.failUnless(len(self.sol.level_order_bottom(None)) == 0)


    #
    def test_with_binary_tree(self):
        binary_tree = src.data_structure.binary_tree()
        binary_tree.add_node(9)
        binary_tree.add_node(3)
        binary_tree.add_node(20)
        binary_tree.add_node(15)
        binary_tree.add_node(25)

        ret_list = self.sol.level_order_bottom(binary_tree.get_root())
        self.failUnless(compare(ret_list[0], [15, 25]))
        self.failUnless(compare(ret_list[1], [3, 20]))
        self.failUnless(compare(ret_list[2], [9]))