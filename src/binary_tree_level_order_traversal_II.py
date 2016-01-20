#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

'''
Given a binary tree, return the bottom-up level order traversal of its nodes' values.
(ie, from left to right, level by level from leaf to root).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
'''

from collections import deque


class Solution(object):
    def level_order_bottom(self, root):
        """
        :type root: tree_node
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        queue = deque([root])
        curr = 1
        next = 0
        ret = []
        tmp = []
        while len(queue) != 0:
            node = queue.popleft()
            tmp.append(node.val)
            curr -= 1
            if node.left:
                queue.append(node.left)
                next += 1
            if node.right:
                queue.append(node.right)
                next += 1
            if curr == 0:
                curr = next
                next = 0
                ret.insert(0, tmp)
                tmp = []
        return ret
