#!/usr/bin/env python2.7


'''
unit test for reversing list
'''


import src.data_structure
import src.utilities
import unittest


class reverse_list_test(unittest.TestCase):
    sol = src.utilities.Helper()

    def test1(self):
        self.failUnless(self.sol.reverse_list(None) is None)

    def test2(self):
        head = src.data_structure.list_node(1)
        list_before = src.data_structure.linked_list(head)
        list_after = src.data_structure.linked_list(self.sol.reverse_list(head))
        self.failUnless(list_before == list_after)

    def test3(self):
        head = src.data_structure.list_node(1)
        list_before = src.data_structure.linked_list(head)
        node2 = src.data_structure.list_node(2)
        list_before.insert_right(node2)
        node3 = src.data_structure.list_node(3)
        list_before.insert_right(node3)

        list_after = src.data_structure.linked_list(node3)
        list_after.insert_right(node2)
        list_after.insert_right(head)

        self.failUnless(list_after == src.data_structure.linked_list(self.sol.reverse_list(head)))