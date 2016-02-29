#!/usr/bin/env python2.7


'''
unit test for contains duplicates II
'''


import unittest
import src.contains_duplicates_II

class contains_duplicates_II_test(unittest.TestCase):
    sol = src.contains_duplicates_II.Solution()

    def test_with_none_list(self):
        self.failUnless(self.sol.contains_nearby_duplicates(None, 1) is False)

    def test_with_nums_with_nearby_dupes(self):
        nums = [2, 3, 2, 5]
        self.failUnless(self.sol.contains_nearby_duplicates(nums, 2) is True)

    def test_with_nums_without_nearby_dupes(self):
        nums = [2, 3, 4, 2]
        self.failUnless(self.sol.contains_nearby_duplicates(nums, 1) is False)