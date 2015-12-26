#!/usr/bin/python2.7

'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following is not:
    1
   / \
  2   2
   \   \
   3    3
'''

from data_structure import tree_node

class Solution(object):
    def is_symmetric_helper(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        elif root1 is None or root2 is None:
            return False
        else:
            return (root1.val == root2.val) and \
                    self.is_symmetric_helper(root1.left, root2.right) and \
                    self.is_symmetric_helper(root1.right, root2.left)

    def is_symmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self.is_symmetric_helper(root.left, root.right)