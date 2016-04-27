#!/usr/bin/env python2.7


'''
unit test for longest common prefix strings
'''

import unittest
import src.longest_common_prefix


class longest_common_prefix_test(unittest.TestCase):
    sol = src.longest_common_prefix.Solution()

    def test1(self):
        strs = None
        self.failUnless(self.sol.longest_commone_prefix(strs) == '')

    def test2(self):
        strs = []
        self.failUnless(self.sol.longest_commone_prefix(strs) == '')

    def test3(self):
        strs = ['abcd', 'abc', 'ab']
        self.failUnless(self.sol.longest_commone_prefix(strs) == 'ab')

def main():
    unittest.main()

if __name__ == "__main__":
    main()