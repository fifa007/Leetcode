#!/usr/bin/python2.7

'''
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
'''

__author__ = 'hao.chen'

from data_structure import *

class solution(object):
    def max_depth(self, root):
        '''

        :param root: tree_node
        :return: int
        '''
        if root is None:
            return 0
        return max(self.max_depth(root.left), self.max_depth(root.right)) + 1


if __name__ == "__main__":
    sol = solution()
    root = None
    print sol.max_depth(root)
