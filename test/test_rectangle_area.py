#!/usr/bin/env python2.7

'''
unit test for rectangle area
'''


import unittest
import src.rectangle_area


class rectangle_area_test(unittest.TestCase):
    sol = src.rectangle_area.Solution()

    def test_with_separate_rectangles(self):
        A = -2
        B = -2
        C = 2
        D = 2
        E = -4
        F = -4
        G = -3
        H = -3
        self.failUnless(self.sol.compute_area(A, B, C, D, E, F, G, H) == 17)

    def test_with_overlapped_rectangles(self):
        A = -2
        B = -2
        C = 2
        D = 2
        E = -1
        F = -1
        G = 3
        H = 3
        self.failUnless(self.sol.compute_area(A, B, C, D, E, F, G, H) == 23)