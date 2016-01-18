#!/usr/bin/env python2.7


'''
Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary
tree is defined as a binary tree in which the depth of
the two subtrees of every node never differ by more than 1.
'''

import math

class Solution(object):
    def is_balanced_binary_tree(self, root):
        """
        :type root: tree_node
        :rtype: bool
        """
        if root is None:
            return True
        return abs(self.tree_height(root.left) - self.tree_height(root.right)) <= 1 \
                and self.is_balanced_binary_tree(root.left) \
                and self.is_balanced_binary_tree(root.right)

    def tree_height(self, root):
        if root is None:
            return 0
        return 1 + max(self.tree_height(root.left), self.tree_height(root.right))
