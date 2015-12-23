#!/usr/bin/python2.7

'''
Invert a binary tree.

     4
   /   \
  2     7
 / \   / \
1   3 6   9
to
     4
   /   \
  7     2
 / \   / \
9   6 3   1
'''

__author__ = 'hao.chen'

from data_structure import *

class Solution(object):
    def invert_tree(self, root):
        if root is None:
            return None
        ret = tree_node(root.val)
        ret.left = self.invert_tree(root.right)
        ret.right = self.invert_tree(root.left)
        return ret



if __name__ == "__main__":
    sol = Solution()
    sol.invert_tree(None)
