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


#definition for list node
class list_node(object):
    def __init__(self, x = None, next = None):
        self.val = x
        self.next = None

    def __eq__(self, other):
        return self.val == other

    def get_data(self):
        return self.val

    def get_next(self):
        return self.next

    def set_next(self, node):
        self.next = node

#implementation of linked list
class linked_list(object):
    def __init__(self, head = None):
        self.head = head

    def insert(self, data):
        node = list_node(data)
        node.set_next(self.head)
        self.head = node

    def get_size(self):
        curr = self.head
        count = 0
        while curr:
            count += 1
            curr = curr.get_next()
        return count

    def search(self, data):
        curr = self.head
        while curr:
            if curr.get_data() == data:
                break
            curr = curr.get_next()
        return curr

    def delete(self, data):
        curr = self.head
        prev = None
        while curr:
            if curr.get_data() == data:
                break
            prev = curr
            curr = curr.get_next()
        if curr is not None:
            prev.next = curr.get_next()




