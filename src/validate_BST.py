#!/usr/bin/env python2.7

'''
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Example 1:
    2
   / \
  1   3
Binary tree [2,1,3], return true.
Example 2:
    1
   / \
  2   3
Binary tree [1,2,3], return false.
'''


class Solution(object):
    def get_right_most(self, root):
        if root is None:
            return None
        curr = root
        while curr.right:
            curr = curr.right
        return curr

    def get_left_most(self, root):
        if root is None:
            return None
        curr = root
        while curr.left:
            curr = curr.left
        return curr

    def is_valid_BST(self, root):
        if root is None:
            return True
        r = self.get_left_most(root.right)
        l = self.get_right_most(root.left)
        if r and l:
            return l.val < root.val and root.val < r.val \
                   and self.is_valid_BST(root.left) and self.is_valid_BST(root.right)
        elif r:
            return root.val < r.val and self.is_valid_BST(root.right)
        elif l:
            return l.val < root.val and self.is_valid_BST(root.left)
        else:
            return True