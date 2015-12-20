#!/usr/bin/python2.7

'''
unit test for same tree
'''
from src.same_tree import *

__author__ = 'hao.chen'

import unittest

class is_same_tree_tests(unittest.TestCase):

    def test_same_tree(self):
        n1 = tree_node(3)
        n1left = tree_node(0)
        n1right = tree_node(2)
        n1.left = n1left
        n1.right = n1right
        n2 = tree_node(1)
        n2left = tree_node(0)
        n2right = tree_node(2)
        n2.left = n2left
        n2.right = n2right
        sol = solution()
        self.failUnless(sol.is_same_tree(n1, n2) == False)

def main():
    unittest.main()


if __name__ == "__main__":
    main()

