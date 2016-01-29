#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-


'''
Given a binary tree and a sum, determine if the tree has a root-to-leaf
path such that adding up all the values along the path equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
'''


class Solution(object):
    def has_path_sum(self, root, sum):
        if root is None:
            return False
        curr_sum = 0
        return self.helper(root, curr_sum, sum)

    def helper(self, root, curr_sum, sum):
        if root is None:
            return False
        if root.left is None and root.right is None:
            curr_sum += root.val
            if curr_sum == sum:
                return True
            else:
                curr_sum -= root.val
                return False

        return self.helper(root.left, curr_sum + root.val, sum) or \
               self.helper(root.right, curr_sum + root.val, sum)



