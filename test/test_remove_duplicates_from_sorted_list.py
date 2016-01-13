#!/usr/bin/env python2.7


'''
unit test for remove_duplicates_from_sorted_list
'''

import src.remove_duplicates_from_sorted_list
import src.data_structure
import unittest


class remove_duplicates_from_sorted_list_test(unittest.TestCase):
    sol = src.remove_duplicates_from_sorted_list.Solution()

    #
    def test_with_null_list(self):
        self.failUnless(not self.sol.remove_duplicates_from_sorted_list(None))

    #
    def test_with_single_list(self):
        head = src.data_structure.list_node(1)
        self.failUnless(self.sol.remove_duplicates_from_sorted_list(head) == head)

    #
    def test_with_sorted_list(self):
        head = src.data_structure.list_node(1)
        head.next = src.data_structure.list_node(1)
        head.next.next = src.data_structure.list_node(2)
        head.next.next.next = src.data_structure.list_node(2)
        head.next.next.next.next = src.data_structure.list_node(3)

        ret = self.sol.remove_duplicates_from_sorted_list(head)
        self.failUnless(ret == head)
        self.failUnless(ret.next.val == 2)
        self.failUnless(ret.next.next.val == 3)