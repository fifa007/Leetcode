#!/usr/bin/env python2.7


'''
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path
from the root node down to the nearest leaf node.
'''

import math

class Solution(object):
    def min_depth(self, root):
        if root is None:
            return 0
        elif root.left is None or root.right is None:
            return 1 + self.min_depth(root.left if root.right is None else root.right)
        else:
            return 1 + min(self.min_depth(root.left), self.min_depth(root.right))

        