#!/usr/bin/env python2.7


'''
unit tests for intersection_of_two_linked_list
'''

import unittest
import src.data_structure
import src.intersection_of_two_linked_list


class intersection_of_two_linked_list_test(unittest.TestCase):
    sol = src.intersection_of_two_linked_list.Solution()

    def test_with_null_list(self):
        self.failUnless(self.sol.get_intersection(None, None) == None)

    def test_with_lists(self):
        linked_list1 = src.data_structure.linked_list()
        linked_list1.insert(5)
        linked_list1.insert(3)
        linked_list1.insert(2)

        linked_list2 = src.data_structure.linked_list()
        linked_list2.insert(5)

        node = self.sol.get_intersection(linked_list1.get_head(), linked_list2.get_head())
        self.failUnless(self.sol.get_intersection(linked_list1.get_head(), None) == None)
        self.failUnless(node.val == 5)