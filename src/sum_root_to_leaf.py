#!/usr/bin/env python2.7


'''
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

For example,

    1
   / \
  2   3
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = 12 + 13 = 25.
'''


class Solution(object):
    def helper(self, root, sum):
        if root is None:
            return 0
        sum = sum*10 + root.val
        if root.left is None and root.right is None:
            return sum
        return self.helper(root.left, sum) + self.helper(root.right, sum)

    def sum_root_to_leaf(self, root):
        return self.helper(root, 0)
