#!/usr/bin/env python2.7

'''
unit test for majority_element
'''

import unittest
import src.majority_element

class majority_element_test(unittest.TestCase):
    sol = src.majority_element.Solution()

    #test with single element
    def test_with_single_element(self):
        self.failUnless(self.sol.majority_element([1]) == 1)

    #test with multiple elements
    def test_with_multiple_elements(self):
        self.failUnless(self.sol.majority_element([1,1,2,2,2]) == 2)

def main():
    unittest.main()

if __name__ == "__main__":
    main()