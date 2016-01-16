#!/usr/bin/env python2.7

'''
Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists.
'''

class Solution(object):
    def merge_two_sorted_lists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None or l2 is None:
            return l1 if l1 is not None else l2
        h = None
        curr = None
        while l1 and l2:
            if l1.val < l2.val:
                if h is None:
                    h = l1
                    curr = h
                else:
                    curr.next = l1
                    curr = curr.next
                l1 = l1.next
            else:
                if h is None:
                    h = l2
                    curr = h
                else:
                    curr.next = l2
                    curr = curr.next
                l2 = l2.next
        while l1:
            curr.next = l1
            curr = curr.next
            l1 = l1.next
        while l2:
            curr.next = l2
            curr = curr.next
            l2 = l2.next
        curr.next = None
        return h

