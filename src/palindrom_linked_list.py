#!/usr/bin/env python2.7


'''
Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?
'''


import src.data_structure
import src.utilities


class Solution(object):
    def is_palindrom_linked_list(self, head):
        if head is None or head.next is None:
            return True
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        if fast:
            slow = slow.next
        reverse = src.utilities.Helper().reverse_list(slow)
        while reverse:
            if reverse.val != head.val:
                return False
            reverse = reverse.next
            head = head.next
        return True