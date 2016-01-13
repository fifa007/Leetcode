#!/usr/bin/env python2.7

'''
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
'''


import src.data_structure


class Solution(object):
    def remove_duplicates_from_sorted_list(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        p = head
        p_next = head.next
        while p_next is not None:
            if p_next.val != p.val:
                p.next = p_next
                p = p_next
            p_next = p_next.next

        p.next = None
        return head