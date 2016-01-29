#!/usr/bin/env python2.7


'''
unit test for path sum
'''

import unittest
import src.data_structure
import src.path_sum


class path_sum_test(unittest.TestCase):
    sol = src.path_sum.Solution()

    def test_with_null_tree(self):
        self.failUnless(self.sol.has_path_sum(None, 1) == False)


    def test_with_root_only(self):
        bst = src.data_structure.binary_search_tree()
        bst.add_node(1)
        self.failUnless(self.sol.has_path_sum(bst.get_root(), 1) == True)

    def test_with_binary_tree(self):
        bst = src.data_structure.binary_search_tree()
        bst.add_node(15)
        bst.add_node(11)
        bst.add_node(21)
        bst.add_node(9)
        bst.add_node(13)
        self.failUnless(self.sol.has_path_sum(bst.get_root(), 35) == True)
        self.failUnless(self.sol.has_path_sum(bst.get_root(), 22) == False)