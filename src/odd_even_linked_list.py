#!/usr/bin/env python2.7


'''
Given a singly linked list, group all odd nodes together followed by the even nodes.
Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example:
Given 1->2->3->4->5->NULL,
return 1->3->5->2->4->NULL.

Note:
The relative order inside both the even and odd groups should remain as it was in the input.
The first node is considered odd, the second node even and so on ...
'''


class Solution(object):
    def odd_even_list(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        p1 = head
        p2 = head.next
        h = head.next
        while p2 is not None:
            tmp = p2.next
            if tmp is None:
                break
            p1.next = p2.next
            p2.next = tmp.next
            p1 = tmp
            p2 = p1.next
        p1.next = h
        return head