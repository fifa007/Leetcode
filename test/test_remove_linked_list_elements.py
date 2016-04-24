#!/usr/bin/env python2.7


'''
unit test for remove linked list elements
'''


import src.remove_linked_list_elements
import unittest
import src.data_structure

class remove_linked_list_elem_test(unittest.TestCase):
    sol = src.remove_linked_list_elements.Solution()

    def test1(self):
        head = src.data_structure.list_node(1)
        list_before = src.data_structure.linked_list(head)
        list_before.insert_right(src.data_structure.list_node(2))
        list_before.insert_right(src.data_structure.list_node(6))
        list_before.insert_right(src.data_structure.list_node(3))
        list_before.insert_right(src.data_structure.list_node(4))
        list_before.insert_right(src.data_structure.list_node(5))
        list_before.insert_right(src.data_structure.list_node(6))

        list_after = self.sol.remove_from_linked_list(head, 6)
        curr = list_after
        self.failUnless(curr.val == 1)
        curr = curr.next
        self.failUnless(curr.val == 2)
        curr = curr.next
        self.failUnless(curr.val == 3)
        curr = curr.next
        self.failUnless(curr.val == 4)
        curr = curr.next
        self.failUnless(curr.val == 5)

def main():
    unittest.main()

if __name__ == "__main__":
    main()