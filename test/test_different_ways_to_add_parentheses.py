#!/usr/bin/env python2.7

'''
unit test for different ways to add parentheses
'''


import unittest
import src.different_ways_to_add_parentheses


class different_ways_to_add_parentheses_test(unittest.TestCase):
    sol = src.different_ways_to_add_parentheses.Solution()

    def test1(self):
        input = "2-1-1"

        output = self.sol.diff_ways_to_compute(input)
        output.sort()
        expected = [0, 2]
        self.failUnless(len(output) == len(expected))
        for i in xrange(len(expected)):
            self.failUnless(output[i] == expected[i])