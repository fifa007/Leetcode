#!/usr/bin/env python2.7


'''
unit test of power_of_three
'''

import unittest
import src.power_of_three


class power_of_three_test(unittest.TestCase):
    sol = src.power_of_three.Solution()

    #
    def test_with_non_positive_number(self):
        self.failUnless(not self.sol.is_power_of_three(-1))

    #
    def test_with_n_not_power_of_3(self):
        self.failUnless(not self.sol.is_power_of_three(5))

    #
    def test_with_n_is_power_of_3(self):
        self.failUnless(self.sol.is_power_of_three(27))

    def test_with_n_is_another_power_of_3(self):
        self.failUnless(self.sol.is_power_of_three(243))


def main():
    unittest.main()

if __name__ == "__main__":
    main()