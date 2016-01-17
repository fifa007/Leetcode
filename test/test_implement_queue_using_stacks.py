#!/usr/bin/env python2.7

'''
unit test for implement_queue_using_stacks
'''

import src.implement_queue_using_stacks
import unittest


class implement_queue_using_stacks_test(unittest.TestCase):
    queue = src.implement_queue_using_stacks.Queue()

    #
    def test_with_empty_queue(self):
        self.failUnless(self.queue.is_empty())

    #
    def test_with_int_queue(self):
        self.queue.push(1)
        self.queue.push(2)

        self.failUnless(self.queue.is_empty() == False)
        self.failUnless(self.queue.size() == 2)
        self.failUnless(self.queue.peek() == 1)
        self.queue.pop()
        self.failUnless(self.queue.size() == 1)