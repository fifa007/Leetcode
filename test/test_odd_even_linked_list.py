#!/usr/bin/env python2.7


'''
unit tests for odd_even_linked_list
'''

import unittest
import src.data_structure
import src.odd_even_linked_list


class odd_even_linked_list_test(unittest.TestCase):
    sol = src.odd_even_linked_list.Solution()


    def test_with_null_list(self):
        self.failUnless(self.sol.odd_even_list(None) is None)

    def test_with_sinle_element_list(self):
        node = src.data_structure.list_node(1)
        self.failUnless(self.sol.odd_even_list(node) == node)

    def test_with_list_containg_odd_nodes(self):
        linked_list = src.data_structure.linked_list()
        linked_list.insert_right(1)
        linked_list.insert_right(2)
        linked_list.insert_right(3)
        linked_list.insert_right(4)
        linked_list.insert_right(5)

        expected_list = src.data_structure.linked_list()
        expected_list.insert_right(1)
        expected_list.insert_right(3)
        expected_list.insert_right(5)
        expected_list.insert_right(2)
        expected_list.insert_right(4)

        new_head = self.sol.odd_even_list(linked_list.get_head())
        expected_head = expected_list.get_head()
        curr1 = new_head
        curr2 = expected_head
        while curr1 is not None and curr2 is not None:
            self.failUnless(curr1 == curr2)
            curr1 = curr1.next
            curr2 = curr2.next
        self.failUnless(curr1 is None and curr2 is None)

