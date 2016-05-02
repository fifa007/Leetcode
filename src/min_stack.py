#!/usr/bin/env python2.7


'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
'''


class Solution(object):
    def __init__(self):
        self.l1 = []
        self.l2 = []

    def push(self, x):
        self.l1.append(x)
        if len(self.l2) == 0 or self.l2[-1] >= x:
            self.l2.append(x)

    def pop(self):
        if len(self.l1) == 0:
            return
        if self.l1[-1] == self.l2[-1]:
            self.l2.pop()
        self.l1.pop()

    def top(self):
        if len(self.l1) == 0:
            return None
        return self.l1[-1]

    def get_min(self):
        if len(self.l2) == 0:
            return None
        return self.l2[-1]