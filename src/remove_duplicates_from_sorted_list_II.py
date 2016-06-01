#!/usr/bin/env python2.7

'''
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.
'''

import src.data_structure

class Solution(object):
    def remove_dupes(self, head):
        if head is None or head.next is None:
            return head
        dummy = src.data_structure.list_node(-1)
        dummy.next = head
        prev = dummy
        p1 = head
        p2 = head.next
        removed = False
        while p2:
            while p2 and p1.val == p2.val:
                removed = True
                p2 = p2.next
            if not p2:
                prev.next = None
                return dummy.next
            if removed:
                prev.next = p2
            else:
                prev.next = p1
                prev = p1
            p1 = p2
            p2 = p2.next
            removed = False
        return dummy.next