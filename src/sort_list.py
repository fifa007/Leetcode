#!/usr/bin/env python2.7

'''
Sort a linked list in O(n log n) time using constant space complexity.
'''


class Solution(object):
    def sort(self, head):
        if head is None or head.next is None:
            return head
        slow = fast = head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        head1 = head
        head2 = slow
        head1 = self.sort(head1)
        head2 = self.sort(head2)
        return self.merge_sort(head1, head2)

    def merge_sort(self, head1, head2):
        if head1 is None and head2 is None:
            return None
        curr1 = head1
        curr2 = head2
        new_head = None
        curr = new_head
        while curr1 and curr2:
            if curr1.val < curr2.val:
                if not new_head:
                    new_head = curr1
                    curr = new_head
                else:
                    curr.next = curr1
                    curr = curr.next
                curr1 = curr1.next
            else:
                if not new_head:
                    new_head = curr2
                    curr = new_head
                else:
                    curr.next = curr2
                    curr = curr.next
                curr2 = curr2.next
        while curr1:
            curr.next = curr1
            curr1 = curr1.next
        while curr2:
            curr.next = curr2
            curr2 = curr2.next
        curr.next = None
        return new_head