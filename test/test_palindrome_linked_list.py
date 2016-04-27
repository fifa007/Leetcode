#!/usr/bin/env python2.7


'''
unit test for palindrome linked list
'''

import src.data_structure
import src.palindrom_linked_list
import unittest


class palindrome_linked_list_test(unittest.TestCase):
    sol = src.palindrom_linked_list.Solution()

    def test1(self):
        head = src.data_structure.list_node(0)
        head.next = src.data_structure.list_node(0)

        self.failUnless(self.sol.is_palindrom_linked_list(head) is True)


def main():
    unittest.main()


if __name__ == "__main__":
    main()