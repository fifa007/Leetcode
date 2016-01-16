#!/usr/bin/env python2.7

'''
unit test for merge_two_sorted_lists
'''

import src.data_structure
import src.merge_two_sorted_lists
import unittest


class merge_two_sorted_lists_test(unittest.TestCase):
    sol = src.merge_two_sorted_lists.Solution()

    #
    def test_with_NULL_lists(self):
        self.failUnless(self.sol.merge_two_sorted_lists(None, None) is None)

    #
    def test_with_single_element_lists(self):
        l1 = src.data_structure.list_node(1)
        l2 = src.data_structure.list_node(2)

        expected_list = src.data_structure.linked_list(src.data_structure.list_node(2))
        expected_list.insert(src.data_structure.list_node(1))

        actual_list = src.data_structure.linked_list(self.sol.merge_two_sorted_lists(l1, l2))
        self.failUnless(expected_list == actual_list)
