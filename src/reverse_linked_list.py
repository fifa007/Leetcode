#!/usr/bin/env python2.7

'''
Reverse a singly linked list.
'''


class Solution(object):
    def reverse_linked_list(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        prev = None
        curr = head
        while curr is not None:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev