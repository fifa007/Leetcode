#!/usr/bin/env python2.7


'''
Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list.
'''


class Solution(object):
    def reverse(self, head, m, n):
        if head is None or head.next is None or m == n:
            return head
        c = 1
        curr = head
        prev = None
        while curr:
            if c == m:
                break
            prev = curr
            curr = curr.next
        if not curr.next:
            return head
        tail = prev
        prev = None
        h = curr
        c = 1
        while c <= n-m+1:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            c += 1
        if h:
            h.next = curr
        if tail:
            tail.next = prev
        else:
            return prev
        return head
