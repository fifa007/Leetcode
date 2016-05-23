#!/usr/bin/env python2.7


'''
Given a binary tree, flatten it to a linked list in-place.

For example,
Given

         1
        / \
       2   5
      / \   \
     3   4   6
The flattened tree should look like:
   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6
'''

class Solution(object):
    def flatten(self, root):
        if root is None:
            return
        self.flatten(root.left)
        self.flatten(root.right)
        if not root.left:
            return
        p = root.left
        while p.right:
            p = p.right
        p.right = root.right
        root.right = root.left
        root.left = None