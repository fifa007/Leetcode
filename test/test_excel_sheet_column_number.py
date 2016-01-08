#!/usr/bin/env python2.7

'''
unit test for excel sheet column number
'''

import unittest
import src.excel_sheet_column_number

class excel_sheet_column_number_test(unittest.TestCase):
    sol = src.excel_sheet_column_number.Solution()

    #null string
    def test_with_null_string(self):
        self.failUnless(self.sol.title_to_number_recursive(None) == 0)
        self.failUnless(self.sol.title_to_number_iterative(None) == 0)

    #string with single char
    def test_with_single_char_string(self):
        self.failUnless(self.sol.title_to_number_iterative('C') == 3)
        self.failUnless(self.sol.title_to_number_recursive('D') == 4)

    #string with mulitple char
    def test_with_multi_chars(self):
        self.failUnless(self.sol.title_to_number_recursive('AA') == 27)
        self.failUnless(self.sol.title_to_number_iterative('AB') == 28)

def main():
    unittest.main()

if __name__ == "__main__":
    main()