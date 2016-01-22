#!/usr/bin/env python2.7

'''
unit test for remove_element
'''

import unittest
import src.remove_element


class remove_element_test(unittest.TestCase):
    sol = src.remove_element.Solution()

    #
    def test_with_empty_list(self):
        self.failUnless(self.sol.remove_element(None, 1) == 0)

    #
    def test_with_list_not_containing_element(self):
        nums = [1, 2, 3]
        self.failUnless(self.sol.remove_element(nums, 4) == 3)

    #
    def test_with_list_containing_element(self):
        nums = [1, 2, 2, 2]
        self.failUnless(self.sol.remove_element(nums, 2) == 1)

    #
    def test_with_list_containing_element_only(self):
        nums = [1, 1, 1]
        self.failUnless(self.sol.remove_element(nums, 1) == 0)