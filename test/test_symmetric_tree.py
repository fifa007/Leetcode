#!/usr/bin/python2.7

'''
unit test for symmetric_tree
'''

import unittest
import src.data_structure
import src.symmetric_tree_recursive
import src.symmetric_tree_iterative


class symmetric_tree_test(unittest.TestCase):

    # test recursive method
    def test_symmetric_tree_recursive(self):
        self.method_factory(src.symmetric_tree_recursive.Solution)

    # test for iterative method
    def test_symmetric_tree_iterative(self):
        self.method_factory(src.symmetric_tree_iterative.Solution)

    def method_factory(self, method_class):
        # null tree
        sol = method_class()
        self.failUnless(sol.is_symmetric(None))

        # one element tree
        r1 = src.data_structure.tree_node(1)
        self.failUnless(sol.is_symmetric(r1))

        # tree
        r1 = src.data_structure.tree_node(1)
        r1.left = src.data_structure.tree_node(2)
        r1.right = src.data_structure.tree_node(3)
        self.failUnless(sol.is_symmetric(r1) == False)

        r1 = src.data_structure.tree_node(1)
        r1_left = src.data_structure.tree_node(2)
        r1_right = src.data_structure.tree_node(2)
        r1_left_left = src.data_structure.tree_node(3)
        r1_left_right = src.data_structure.tree_node(4)
        r1_right_left = src.data_structure.tree_node(4)
        r1_right_right = src.data_structure.tree_node(3)
        r1.left = r1_left
        r1.right = r1_right
        r1_left.left = r1_left_left
        r1_left.right = r1_left_right
        r1_right.left = r1_right_left
        r1_right.right = r1_right_right
        self.failUnless(sol.is_symmetric(r1))

def main(self):
    unittest.main()

if __name__ == "__main__":
    main()
