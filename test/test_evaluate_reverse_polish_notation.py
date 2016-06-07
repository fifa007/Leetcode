#!/usr/bin/env python2.7

'''
unit tests for evalute reverse polish notation
'''


import unittest
import src.evaluate_reverse_polish_notation

class evaluate_reverse_polish_notation_test(unittest.TestCase):
    sol = src.evaluate_reverse_polish_notation.Solution()

    def test1(self):
        self.failUnless(self.sol.calculate(["6", "-132", "/"]) == 0)