#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

'''
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and
w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”

        _______6______
       /              \
    ___2__          ___8__
   /      \        /      \
   0      _4       7       9
         /  \
         3   5
For example, the lowest common ancestor (LCA) of nodes 2 and 8 is 6. Another example is LCA of nodes 2 and 4 is 2,
since a node can be a descendant of itself according to the LCA definition.
'''

class Solution(object):
    def lowest_common_lca(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        high_value = max(p.val, q.val)
        low_value = min(p.val, q.val)
        if low_value <= root.val <= high_value and \
                root.left is not None and \
                root.right is not None:
            return root
        if root.val > high_value:
            return self.lowest_common_lca(root.left, p, q)
        if root.val < low_value:
            return self.lowest_common_lca(root.right, p, q)
        return None



