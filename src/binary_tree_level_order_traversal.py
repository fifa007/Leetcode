#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

'''
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.
'''

from collections import deque

class Solution(object):
    def binary_tree_level_order_traversal(self, root):
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
            curr -= 1
            tmp.append(node.val)
            if node.left is not None:
                queue.append(node.left)
                next += 1
            if node.right is not None:
                queue.append(node.right)
                next += 1
            if curr == 0:
                ret.append(tmp)
                tmp = []
                curr = next
                next = 0
        return ret