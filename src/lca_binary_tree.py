#!/usr/bin/env python2.7

'''
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between
two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a
node to be a descendant of itself).”

        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2       0       8
         /  \
         7   4
For example, the lowest common ancestor (LCA) of nodes 5 and 1 is 3.
Another example is LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
'''


class Solution(object):
    def lca_binary_tree(self, root, p, q):
        if root is None or (not p and not q):
            return None
        if not p or not q:
            return p if not q else q
        if root == q or root == q:
            return root
        L = self.lca_binary_tree(root.left, p, q)
        R = self.lca_binary_tree(root.right, p, q)
        if L and R:
            return root
        return L if not R else R