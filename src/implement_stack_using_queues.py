#!/usr/bin/env python2.7

'''
Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.
Notes:
You must use only standard operations of a queue -- which means only push to back,
peek/pop from front, size, and is empty operations are valid.
Depending on your language, queue may not be supported natively.
You may simulate a queue by using a list or deque (double-ended queue),
as long as you use only standard operations of a queue.
You may assume that all operations are valid (for example,
no pop or top operations will be called on an empty stack).
'''

from collections import deque

class Solution(object):
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x):
        self.q1.append(x)

    def pop(self):
        while len(self.q1) != 0:
            self.q2.append(self.q1.popleft())
        self.q2.pop()

    def top(self):
        while len(self.q1) != 0:
            self.q2.append(self.q1.popleft())
        return self.q2[-1]

    def empty(self):
        return len(self.q1) == 0 and len(self.q2) == 0