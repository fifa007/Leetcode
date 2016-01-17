#!/usr/bin/env python2.7

'''
Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
Notes:
You must use only standard operations of a stack -- which means only push to top,
peek/pop from top, size, and is empty operations are valid.Depending on your language,
stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue),
as long as you use only standard operations of a stack.You may assume that all operations are valid
(for example, no pop or peek operations will be called on an empty queue).
'''

class Stack(object):
    def __init__(self):
        self.__storage = []

    def push(self, x):
        self.__storage.append(x)

    def pop(self):
        self.__storage.pop()

    def top(self):
        if len(self.__storage) == 0:
            return None
        return self.__storage[-1]

    def is_empty(self):
        return len(self.__storage) == 0

    def size(self):
        return len(self.__storage)

class Queue(object):
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def push(self, x):
        self.s1.push(x)

    def pop(self):
        if self.s2.is_empty():
            while self.s1.is_empty() == False:
                self.s2.push(self.s1.top())
                self.s1.pop()
        self.s2.pop()

    def peek(self):
        if self.s1.is_empty() and self.s2.is_empty():
            return None
        elif self.s2.is_empty():
            while self.s1.is_empty() == False:
                self.s2.push(self.s1.top())
                self.s1.pop()
        return self.s2.top()

    def is_empty(self):
        return self.s1.is_empty() and self.s2.is_empty()

    def size(self):
        return self.s1.size() + self.s2.size()
