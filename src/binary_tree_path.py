#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

'''
Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

["1->2->5", "1->3"]
'''


class Solution(object):
    def helper(self, node, char_list, res):
        if node is None:
            return []
        if node.left is None and node.right is None:
            char_list.append(str(node.val))
            res.append('->'.join(char_list))
            del char_list[-1]
            return
        char_list.append(str(node.val))
        if node.left:
            self.helper(node.left, char_list, res)
        if node.right:
            self.helper(node.right, char_list, res)
        del char_list[-1]

    def get_root_to_left_path(self, root):
        char_list = []
        res = []
        self.helper(root, char_list, res)
        return res
    


