#!/usr/bin/env python2.7


'''
unit test for implement stack using queues
'''


import unittest
import src.implement_stack_using_queues

class implement_stack_using_queues_test(unittest.TestCase):
    sol = src.implement_stack_using_queues.Solution()

    def test_with_basic_stack(self):
        self.sol.push(1)
        self.sol.push(2)
        self.failUnless(self.sol.top() == 2)
        self.sol.pop()
        self.failUnless(self.sol.top() == 1)
        self.sol.push(3)
        self.failUnless(self.sol.top() == 3)