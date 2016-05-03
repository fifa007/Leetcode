#!/usr/bin/env python2.7


'''
unit tests for comparing version numbers
'''

import unittest
import src.compare_version_numbers


class compare_version_test(unittest.TestCase):
    sol = src.compare_version_numbers.Solution()

    def test1(self):
        v1 = "1.0"
        v2 = "1"
        self.failUnless(self.sol.compare_versions(v1, v2) == 0)

    def test2(self):
        v1 = "1.1"
        v2 = "1"
        self.failUnless(self.sol.compare_versions(v1, v2) == 1)

    def test3(self):
        v1 = "1.2.3.4"
        v2 = "1.2.3"
        self.failUnless(self.sol.compare_versions(v1, v2) == 1)

def main():
    unittest.main()

if __name__ == "__main__":
    main()