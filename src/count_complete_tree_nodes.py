#!/usr/bin/env python2.7

'''
Given a complete binary tree, count the number of nodes.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled,
and all nodes in the last level are as far left as possible.
It can have between 1 and 2h nodes inclusive at the last level h.
'''


class Solution(object):
    '''
    Find depth of left most node for right sub tree of current root
    '''
    def find_depth(self, root):
        if root is None:
            return 0
        curr = root.right
        dep = 0
        while curr:
            dep += 1
            curr = curr.right
        return dep

    def count(self, root):
        if root is None:
            return 0

        dep = 0
        curr = root
        while curr:
            dep += 1
            curr = curr.left

        curr = root
        curr_dep = 1
        ret = 0
        while curr_dep < dep:
            h = self.find_depth(curr)
            if h + curr_dep == dep:
                ret += pow(2, h-1)
                curr_dep += 1
                curr = curr.right
            else:
                curr = curr.left
                curr_dep += 1
        return ret + pow(2, dep-1)