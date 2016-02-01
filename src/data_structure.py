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

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        return False

    def __ne__(self, other):
        return not self.__eq__(other)


class binary_search_tree(object):
    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    def add_node(self, val):
        if self.root is None:
            self.root = tree_node(val)
        else:
            self._add_node(val, self.root)

    def _add_node(self, val, node):
        if val < node.val:
            if node.left is not None:
                self._add_node(val, node.left)
            else:
                node.left = tree_node(val)
        else:
            if node.right is not None:
                self._add_node(val, node.right)
            else:
                node.right = tree_node(val)

    def find_node(self, val):
        if self.root is not None:
            return self._find_node(val, self.root)
        else:
            return None

    def _find_node(self, val, node):
        if val == node.val:
            return node
        elif val < node.val:
            return self._find_node(val, node.left)
        else:
            return self._find_node(val, node.right)

    def delete_tree(self):
        self.root = None

    def print_tree(self):
        if self.root is not None:
            self._print_tree(self.root)

    def _print_tree(self, node):
        if node is not None:
            self._print_tree(node.left)
            print node.val + ' '
            self._print_tree(node.right)
            

class Interval(object):
    def __init__(self, s = 0, e = 0):
        self.start = s
        self.end = e

