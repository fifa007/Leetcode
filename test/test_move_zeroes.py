#!/usr/bin/python2.7

'''
unit test for move zeroes
'''

import unittest
import src.move_zeroes

class move_zeroes_test(unittest.TestCase):
    def test_move_zeroes(self):
        # empty list
        nums = None
        sol = src.move_zeroes.Solution()
        sol.move_zeroes(nums)
        self.failUnless(nums is None)

        # single element list
        nums = [1]
        sol = src.move_zeroes.Solution()
        sol.move_zeroes(nums)
        self.failUnless(nums == [1])

        # multiple elements list
        nums = [0, 1, 0, 3, 12]
        expected_nums = [1, 3, 12, 0, 0]
        sol = src.move_zeroes.Solution()
        sol.move_zeroes(nums)
        self.failUnless(nums == expected_nums)

def main():
    unittest.main()


if __name__ == "__main__":
    main()