#!/usr/bin/env python2.7

'''
unit tests for unique path II
'''

import unittest
import src.unique_path_II

class unique_path_II_test(unittest.TestCase):
    sol = src.unique_path_II.Solution()

    def test1(self):
        nums = [[1], [0]]
        cnt = self.sol.unique_path(nums)
        self.failUnless(cnt == 0)