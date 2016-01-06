#!/usr/bin/env python2.7

'''
unit test for delete_node_in_linked_list
'''

import unittest
import src.data_structure
import src.delete_node_in_linked_list


class delete_node_in_linked_list_test(unittest.TestCase):
    sol = src.delete_node_in_linked_list.Solution()

    #empty node
    def test_with_empty_node(self):
       self.failUnless(self.sol.delete_node(None) is None)

    #tail node/single node
    def test_with_tail_node(self):
        n = src.data_structure.list_node(1)
        self.sol.delete_node(n)
        self.failUnless(n.val == 1)

def main():
    unittest.main()


if __name__ == "__main__":
    main()