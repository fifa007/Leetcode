#!/usr/bin/env python2.7


'''
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
'''

import src.data_structure

class Solution(object):
    def sort_helper(self, nums, start, end):
        if start > end:
            return None
        mid = start + (end - start)/ 2
        root = src.data_structure.tree_node(nums[mid])
        root.left = self.sort_helper(nums, start, mid-1)
        root.right = self.sort_helper(nums, mid+1, end)
        return root

    def convert_to_bst(self, nums):
        return self.sort_helper(nums, 0, len(nums)-1)