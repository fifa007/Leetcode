#!/usr/bin/env python2.7


'''
unit tests for max_sub_array_equals_k
'''


import unittest
import src.maximum_sub_array_sum_eqauls_k

class max_sub_array_equals_k_test(unittest.TestCase):
    sol = src.maximum_sub_array_sum_eqauls_k.Solution()

    def test_with_empty_array(self):
        self.failUnless(self.sol.max_subarray(None, 1) == 0)

    def test_with_array_1(self):
        nums = [1, -1, 5, -2, 3]
        k = 3
        self.failUnless(self.sol.max_subarray(nums, k) == 4)

    def test_with_array_2(self):
        nums = [-2, -1, 2, 1]
        k = 1
        self.failUnless(self.sol.max_subarray(nums, k) == 2)