#!/usr/bin/env python2.7

'''
Given a binary tree, return the preorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,2,3].
'''


class Solution(object):
    def preorder_traversal(self, root):
        if root is None:
            return None
        s = [root]
        ret = []
        while len(s) != 0:
            tmp = s.pop()
            ret.append(tmp.val)
            if tmp.right:
                s.append(tmp.right)
            if tmp.left:
                s.append(tmp.left)
        return ret