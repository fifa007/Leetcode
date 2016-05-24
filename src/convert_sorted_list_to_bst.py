#!/usr/bin/env python2.7


'''
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
'''

import src.data_structure

class Solution(object):
    def sorted_list_to_bst(self, head):
        if head is None:
            return None
        if head.next is None:
            return src.data_structure.tree_node(head.val)
        slow = fast = head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return None
        prev.next = None
        root = src.data_structure.tree_node(slow.val)
        root.left = self.sorted_list_to_bst(head)
        root.right = self.sorted_list_to_bst(slow.next)
        return root

