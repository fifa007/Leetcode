#!/usr/bin/env python2.7


'''
Remove all elements from a linked list of integers that have value val.

Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5
'''

class Solution(object):
    def remove_from_linked_list(self, head, value):
        if head is None or value is None:
            return None
        while head and head.val == value:
            head = head.next
        if head is None:
            return None
        prev = head
        curr = head.next
        while curr:
            if curr.val == value:
                curr = curr.next
                continue
            prev.next = curr
            prev = curr
            curr = curr.next
        prev.next = None
        return head