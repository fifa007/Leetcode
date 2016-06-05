#!/usr/bin/env python2.7

'''
unit tests for sort list
'''


import unittest
import src.data_structure
import src.sort_list

class sort_list_test(unittest.TestCase):
    sol = src.sort_list.Solution()

    def test1(self):
        input_list = src.data_structure.linked_list()
        input_list.insert(1)
        input_list.insert(2)
        expected_list = src.data_structure.linked_list()
        expected_list.insert_right(1)
        expected_list.insert_right(2)
        actual_list = self.sol.sort(input_list.get_head())
        self.failUnless(expected_list.get_head() == actual_list)