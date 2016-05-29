#!/usr/bin/env python2.7


'''
Given a binary tree, return the zigzag level order traversal of its nodes' values.
(ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
'''


class Solution(object):
    def zigzag_traversal(self, root):
        if root is None:
            return []
        ret = []
        l = []
        left_right = True
        q = [root]
        curr = 1
        next = 0
        while len(q) != 0:
            node = q.pop(0)
            curr -= 1
            if left_right:
                l.append(node.val)
            else:
                l.insert(0, node.val)
            if node.left:
                q.append(node.left)
                next += 1
            if node.right:
                q.append(node.right)
                next += 1
            if curr == 0:
                curr = next
                next = 0
                ret.append(l)
                l = []
                left_right = not left_right
        return ret