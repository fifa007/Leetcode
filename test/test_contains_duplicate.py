#!/usr/bin/env python2.7

'''
unit test for contains_duplicate
'''


import unittest
import src.contains_duplicate

class contains_duplicate_test(unittest.TestCase):
    sol = src.contains_duplicate.Solution()

    #null list
    def test_with_null_list(self):
        self.failUnless(self.sol.contains_duplicate(None) == False)

    #list with single element
    def test_with_single_element_list(self):
        self.failUnless(self.sol.contains_duplicate([1]) == False)

    #list with duplicate elements
    def test_with_duplicate_element_list(self):
        self.failUnless(self.sol.contains_duplicate([1,1]) == True)

def main():
    unittest.main()

if __name__ == "__main__":
    main()