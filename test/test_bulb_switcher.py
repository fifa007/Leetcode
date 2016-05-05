#!/usr/bin/env python2.7


'''
unit test for bulb switch
'''


import unittest
import src.bulb_switcher

class bulb_switcher_test(unittest.TestCase):
    sol = src.bulb_switcher.Solution()

    def test1(self):
        self.failUnless(self.sol.bulb_switch(3) == 1)