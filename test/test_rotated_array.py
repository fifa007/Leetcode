#!/usr/bin/env python2.7


'''
unit test for rotated array
'''


import src.rotated_array
import unittest


class rotated_array_test(unittest.TestCase):
    sol = src.rotated_array.Solution()


    def test1(self):
        nums = [1, 2]
        k = 1
        self.sol.rotate(nums, k)
        self.failUnless(nums == [2, 1])