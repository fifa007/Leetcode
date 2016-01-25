#1/usr/bin/env python2.7


'''
Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Note:
Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.
'''


import math
import sys


def get_closest(target, val1, val2):
    if abs(target - val1) <= abs(target - val2):
        return val1
    else:
        return val2


class Solution(object):
    def find_closest_value_in_BST(self, root, target):
        if root is None:
            return None
        if root.left is None and root.right is None:
            return root.val
        elif root.left is None or root.right is None:
            node = root.left if root.left is not None else root.right
            return self.get_closest(target, self.closestValue(node, target), root.val)
        if target == root.val:
            return root.val
        elif target < root.val:
            return get_closest(target, self.find_closest_value_in_BST(root.left, target), root.val)
        else:
            return get_closest(target, self.find_closest_value_in_BST(root.right, target), root.val)
