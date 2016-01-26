#!/usr/bin/env python2.7

'''
unit test for remove_duplicates_from_sorted_array
'''

import unittest
import src.remove_duplicates_from_sorted_array


class remove_duplicates_from_sorted_array_test(unittest.TestCase):
    sol = src.remove_duplicates_from_sorted_array.Solution()


    def test_with_null_array(self):
        self.failUnless(self.sol.remove_duplicates(None) == 0)

    def test_with_empty_array(self):
        self.failUnless(self.sol.remove_duplicates([]) == 0)

    def test_with_sorted_array(self):
        nums = [1, 1, 2]
        self.failUnless(self.sol.remove_duplicates(nums) == 2)
        self.failUnless(nums[0] == 1)
        self.failUnless(nums[1] == 2)