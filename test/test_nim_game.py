#!/usr/bin/env python2.7

import unittest
import src.nim_game

class nim_game_test(unittest.TestCase):
    sol = src.nim_game.Solution()

    #n = -1
    def test_with_negative_stones(self):
        self.failUnless(self.sol.can_win_nim(-1) == False)

    #n = 0
    def test_with_zero_stones(self):
        self.failUnless(self.sol.can_win_nim(0) == False)

    #n = 2
    def test_with_two_stones(self):
        self.failUnless(self.sol.can_win_nim(2))

    #n = 4
    def test_with_four_stones(self):
        self.failUnless(not self.sol.can_win_nim(4))

def main():
    unittest.main()


if __name__ == "__main__":
    main()