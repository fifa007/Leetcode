#!/usr/bin/env python2.7

'''
unit test for permutations
'''


import unittest
import src.permutations


class permutations_test(unittest.TestCase):
    sol = src.permutations.Solution()

    def test1(self):
        nums = [1, 2]
        actual = self.sol.get_permutations(nums)