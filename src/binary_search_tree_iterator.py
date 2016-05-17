#!/usr/bin/env python2.7


'''
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
'''

class Solution(object):
    def __init__(self, root):
        self.s = []
        while root:
            self.s.append(root)
            root = root.left

    def has_next(self):
        return len(self.s) != 0

    def next(self):
        tmp = self.s.pop()
        if tmp.right:
            curr = tmp.right
            while curr:
                self.s.append(curr)
                curr = curr.left
        return tmp.val
