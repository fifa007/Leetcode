#!/usr/bin/env python2.7

'''
unit tests for data_structure
'''


import src.data_structure
import unittest

class data_structur_test(unittest.TestCase):
    sol = src.data_structure.binary_tree()
    sol.add_node(5)

    #
    def test_tree_root(self):
        self.failUnless(self.sol.get_root().val == 5)

    sol.add_node(3)
    sol.add_node(8)

    #
    def test_find_node(self):
        self.failUnless(self.sol.find_node(3).val == 3)
