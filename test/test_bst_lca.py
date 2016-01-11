#!/usr/bin/env python2.7

'''
unit test for bst_lca
'''

import src.bst_lca
import src.data_structure
import unittest

class bst_lca_test(unittest.TestCase):
    sol = src.bst_lca.Solution()

    #root==None
    def test_with_null_root(self):
        self.failUnless(self.sol.lowest_common_lca(None, None, None) == None)

    #
    def test_with_p_q_on_both_sides(self):
        root = src.data_structure.tree_node(5)
        p = src.data_structure.tree_node(3)
        q = src.data_structure.tree_node(8)
        root.left = p
        root.right = q
        self.failUnless(self.sol.lowest_common_lca(root, p, q) == root)

    #
    def test_with_single_node(self):
        root = src.data_structure.tree_node(5)
        p = src.data_structure.tree_node(3)
        q = src.data_structure.tree_node(8)
        self.failUnless(self.sol.lowest_common_lca(root, p, q) == None)

    #
    def test_with_p_q_in_left_tree(self):
        root = src.data_structure.tree_node(10)
        p = src.data_structure.tree_node(5)
        t = src.data_structure.tree_node(3)
        q = src.data_structure.tree_node(8)
        root.left = p
        p.left = t
        p.right = q
        self.failUnless(self.sol.lowest_common_lca(root, p, q) == p)
