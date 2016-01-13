#!/usr/bin/env python2.7


'''
unit test for climbing_stairs
'''

import src.climbing_stairs
import unittest

class climbing_stairs_test(unittest.TestCase):
    sol = src.climbing_stairs.Solution()

    #
    def test_with_0_stair(self):
        self.failUnless(self.sol.climbing_stairs(0) == 0)

    #
    def test_with_1_stair(self):
        self.failUnless(self.sol.climbing_stairs(1) == 1)

    #
    def test_with_2_stairs(self):
        self.failUnless(self.sol.climbing_stairs(2) == 2)

    #
    def test_with_5_stairs(self):
        self.failUnless(self.sol.climbing_stairs(5) == 8)

def main():
    unittest.main()

if __name__ == "__main__":
    main()