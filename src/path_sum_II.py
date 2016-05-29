#!/usr/bin/env python2.7


'''
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
]
'''


class Solution(object):
    def path_sum(self, root, sum):
        if root is None:
            return []
        if not root.left and not root.right and root.val == sum:
            return [[root.val]]
        ret = []
        left = self.path_sum(root.left, sum - root.val)
        for i in xrange(left):
            left[i].insert(0, root.val)
            ret.append(left[i])
        right = self.path_sum(root.right, sum - root.val)
        for i in xrange(right):
            right[i].insert(0, root.val)
            ret.append(right[i])
        return ret