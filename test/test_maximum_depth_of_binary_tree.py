#!/usr/bin/python2.7

__author__ = 'hao.chen'

from src.maximum_depth_of_binary_tree import solution
from src.data_structure import tree_node
import unittest


class max_depth_of_binary_tree_tests(unittest.TestCase):

    def test_maximum_depth_of_binary_tree(self):
        root = tree_node(1)
        root_left = tree_node(2)
        root_right = tree_node(3)
        root.left = root_left
        root.right = root_right
        root_right_left = tree_node(4)
        root.right.left = root_right_left
        sol = solution()
        self.failUnless(sol.max_depth(root) == 3)


def main():
    unittest.main()


if __name__ == "__main__":
    main()