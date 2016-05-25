#!/usr/bin/env python2.7


'''
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between
two nodes v and w as the lowest node in T that has both v and w as descendants
(where we allow a node to be a descendant of itself).”

        _______6______
       /              \
    ___2__          ___8__
   /      \        /      \
   0      _4       7       9
         /  \
         3   5
For example, the lowest common ancestor (LCA) of nodes 2 and 8 is 6. Another example is
LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
'''


class Solution(object):
    def lca_bst(self, root, p, q):
        if root is None or (not p and not q):
            return None
        if not p or not q:
            return p if not q else q
        bigger = max(p.val, q.val)
        smaller = min(p.val, q.val)
        if root.val >= smaller and root.val <= bigger:
            return root
        elif root.val < smaller:
            return self.lca_bst(root.right, p, q)
        else:
            return self.lca_bst(root.left, p, q)