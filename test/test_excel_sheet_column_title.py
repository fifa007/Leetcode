#!/usr/bin/env python2.7

'''
unit tests for excel column sheet title
'''


import src.excel_column_sheet_title
import unittest


class excel_column_sheet_title_test(unittest.TestCase):
    sol = src.excel_column_sheet_title.Solution()

    def test1(self):
        self.failUnless(self.sol.convert(26) == 'Z')

    def test2(self):
        self.failUnless(self.sol.convert(676) == 'YZ')