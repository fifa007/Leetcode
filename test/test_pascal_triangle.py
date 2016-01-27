#!/usr/bin/env python2.7


'''
unit test of pascal's triangle
'''

import unittest
import src.pascal_triangle


class pascal_triangle_test(unittest.TestCase):
    sol = src.pascal_triangle.Solution()

    def test_with_row_number_equals_zero(self):
        self.failUnless(self.sol.generate_pascal_triangle(0) == [])

    def test_with_row_number_equals_one(self):
        self.failUnless(self.sol.generate_pascal_triangle(1) == [[1]])

    def test_with_row_number_equals_two(self):
        self.failUnless(self.sol.generate_pascal_triangle(2) == [[1], [1, 1]])

    def test_with_row_number_equals_three(self):
        self.failUnless(self.sol.generate_pascal_triangle(3) == [[1], [1, 1], [1, 2, 1]])

def main():
    unittest.main()


if __name__ == "__main__":
    main()