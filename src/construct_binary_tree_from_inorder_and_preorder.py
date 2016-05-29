#!/usr/bin/env python2.7

'''
Given preorder and inorder traversal of a tree, construct the binary tree.
'''

import src.data_structure

class Solution(object):
    def helper(self, preorder, preorder_start, preorder_end, inorder, inorder_start, inorder_end):
        if preorder_start > preorder_end and inorder_start > inorder_end:
            return None
        root = src.data_structure.tree_node(preorder[preorder_start])
        i = 0
        while i + inorder_start < len(inorder):
            if inorder[i+inorder_start] == preorder[preorder_start]:
                break
            i += 1
        root.left = self.helper(preorder, preorder_start+1, preorder_start+i,
                                inorder, inorder_start, inorder_start+i-1)
        root.right = self.helper(preorder, preorder_start+i+1, preorder_end,
                                 inorder, inorder_start+i+1, inorder_end)
        return root

    def build_tree(self, preorder, inorder):
        if preorder is None or inorder is None or len(preorder) != len(inorder):
            return None
        return self.helper(preorder, 0, len(preorder)-1, inorder, 0, len(inorder)-1)