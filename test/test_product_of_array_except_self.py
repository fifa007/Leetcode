#!/usr/bin/env python2.7

'''
unit test for product of array except self
'''


import unittest
import src.product_of_array_except_self


class product_of_array_except_self_test(unittest.TestCase):
    sol = src.product_of_array_except_self.Solution()

    def test1(self):
        nums = [1,2,3,4]
        expected = [24,12,8,6]
        self.failUnless(self.sol.product_except_self(nums) == expected)