#!/usr/bin/env python2.7


'''
Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
'''

class Solution(object):
    def rotate(self, head, k):
        if head is None or head.next is None or k == 0:
            return head
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        r = k % length
        if r == 0:
            return head
        slow = fast = head
        s = 0
        while fast.next:
            if s >= k:
                slow = slow.next
            fast = fast.next
            s += 1
        ret = slow.next
        slow.next = None
        fast.next = head
        return ret