#!/usr/bin/env python2.7

'''
utility functions
'''

import src.data_structure


class Helper(object):
    def reverse_list(self, head):
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
    