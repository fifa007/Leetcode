#!/usr/bin/env python2.7


'''
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list,
only nodes itself can be changed.
'''


class Solution(object):
    def swap_nodes_in_pairs_recursive(self, head):
        if head is None or head.next is None:
            return head
        ret = head.next
        head.next = self.swap_nodes_in_pairs_recursive(ret.next)
        ret.next = head
        return ret

    def swap_nodes_in_pairs_iterative(self, head):
        if head is None or head.next is None:
            return head
        ret = head.next
        p1 = head
        prev = head
        while p1 and p1.next:
            p2 = p1.next
            tmp = p2.next
            prev.next = p2
            p2.next = p1
            p1.next = tmp
            prev = p1
            p1 = tmp
        ret.next = head
        return ret
