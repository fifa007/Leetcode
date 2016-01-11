#!/usr/bin/env python2.7

'''
unit test of reverse_linked_list
'''

import unittest
import src.reverse_linked_list
import src.data_structure

class reverse_linked_list_test(unittest.TestCase):
    sol = src.reverse_linked_list.Solution()

    #
    def test_with_null_list(self):
        self.failUnless(self.sol.reverse_linked_list(None) is None)

    #
    def test_with_single_element_list(self):
        head = src.data_structure.list_node(5)
        self.failUnless(self.sol.reverse_linked_list(head) == head)

    #
    def test_with_multiple_elements(self):
        head = src.data_structure.list_node(1)
        head_next = src.data_structure.list_node(2)
        head.next = head_next

        reversed_head = src.data_structure.list_node(2)
        reversed_head_next = src.data_structure.list_node(1)
        reversed_head.next = reversed_head_next
        self.failUnless(self.sol.reverse_linked_list(head) == reversed_head)