#!/usr/bin/env python2.7


'''
You are given two linked lists representing two non-negative numbers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
'''

import src.data_structure

class Solution(object):
    def add_two_numbers(self, l1, l2):
        if l1 is None or l2 is None:
            return l1 if l1 else l2
        ret = None
        curr = None
        carry = 0
        while l1 and l2:
            val = l1.val + l2.val + carry
            if not ret:
                ret = src.data_structure.list_node(val % 10)
                curr = ret
            else:
                curr.next = src.data_structure.list_node(val % 10)
                curr = curr.next
            carry = val / 10
        while l1 or l2:
            tmp = l1.val if l1 else l2.val
            val = tmp + carry
            curr.next = src.data_structure.list_node(val % 10)
            curr = curr.next
            carry = val / 10
        if carry:
            curr.next = src.data_structure.list_node(carry)
            curr = curr.next
        curr.next = None
        return ret