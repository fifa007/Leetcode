#!/usr/bin/env python2.7


'''
Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,3,2].

Note: Recursive solution is trivial, could you do it iteratively?
'''

class Solution(object):
    def inorder_traversal(self, root):
        if root is None:
            return []
        s = []
        while root:
            s.append(root)
            root = root.left
        ret = []
        while len(s) != 0:
            tmp = s.pop()
            ret.append(tmp.val)
            if tmp.right:
                curr = tmp.right
                while curr:
                    s.append(curr)
                    curr = curr.left
        return ret