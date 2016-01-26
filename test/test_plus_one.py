#!/usr/bin/env python2.7

'''
unit test for plus one
'''

import unittest
import src.plus_one


class plus_one_test(unittest.TestCase):
    sol = src.plus_one.Solution()

    def test_with_empty_list(self):
        self.failUnless(self.sol.plus_one([]) == [])

    def test_with_9(self):
        self.failUnless(self.sol.plus_one([9]) == [1, 0])


def main():
    unittest.main()

if __name__ == "__main__":
    main()