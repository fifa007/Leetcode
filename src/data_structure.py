#!/usr/bin/python2.7

'''
Definition for common data structure
'''

__author__ = 'hao.chen'

#definition for tree node
class tree_node(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


#definition for single-linked list
class list_node(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __eq__(self, other):
        return self.val == other


