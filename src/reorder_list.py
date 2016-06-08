#!/usr/bin/env python2.7


'''
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You must do this in-place without altering the nodes' values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.
'''


class Solution(object):
    def reverse(self, head):
        if head is None or head.next is None:
            return head
        prev = None
        curr = head
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev

    def reorder_list(self, head):
        if head is None or head.next is None:
            return
        slow = fast = head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = None
        l = self.reverse(slow)
        curr = head
        p = head.next
        from_p = False
        while p and l:
            if from_p:
                curr.next = p
                curr = curr.next
                p = p.next
            else:
                curr.next = l
                curr = curr.next
                l = l.next
            from_p = not from_p
        while p:
            curr.next = p
            curr = curr.next
            p = p.next
        while l:
            curr.next = l
            curr = curr.next
            l = l.next
        curr.next = None
        return