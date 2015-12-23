#!/usr/bin/python2.7

'''
unit test for invert_binary_tree
'''

__author__ = 'hao.chen'


import unittest
import src.data_structure
import src.same_tree
import src.invert_binary_tree


class invert_binary_tree_test(unittest.TestCase):

    def test_invert_binary_tree(self):
        root1 = src.data_structure.tree_node(4)
        root1.left = src.data_structure.tree_node(2)
        root1.right = src.data_structure.tree_node(7)
        root2 = src.data_structure.tree_node(4)
        root2.left = src.data_structure.tree_node(7)
        root2.right = src.data_structure.tree_node(2)
        sol1 = src.invert_binary_tree.Solution()
        root3 = sol1.invert_tree(root1)
        sol2 = src.same_tree.solution()
        self.failUnless(sol2.is_same_tree(root2, root3))

def main():
    unittest.main()


if __name__ == "__main__":
    main()
