#!/usr/bin/python2.7

'''
Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical and the nodes have the same value.
'''

__author__ = 'hao.chen'

class tree_node(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class solution(object):
    def is_same_tree(self, p, q):
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False
        else:
            return (p.val == q.val) and self.is_same_tree(p.left, q.left) and self.is_same_tree(p.right, q.right)


if __name__ == "__main__":
    n1 = tree_node(3)
    n1left = tree_node(0)
    n1right = tree_node(2)
    n1.left = n1left
    n1.right = n1right
    n2 = tree_node(1)
    n2left = tree_node(0)
    n2right = tree_node(2)
    n2.left = n2left
    n2.right = n2right
    sol = solution()
    if sol.is_same_tree(n1, n2):
        print "same tree"
    else:
        print 'different tree'
