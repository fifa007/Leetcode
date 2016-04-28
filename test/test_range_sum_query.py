#!/usr/bin/env python2.7

'''
unit test for range sum query
'''

import unittest
import src.range_sum_query_immutable

class range_sum_query_test(unittest.TestCase):
    nums = [-2, 0, 3, -5, 2, -1]
    sol = src.range_sum_query_immutable.num_array(nums)

    def test1(self):
        self.failUnless(self.sol.range_sum_query(0, 2) == 1)
        self.failUnless(self.sol.range_sum_query(2, 5) == -1)
        self.failUnless(self.sol.range_sum_query(0, 5) == -3)