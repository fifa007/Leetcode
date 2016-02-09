#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

'''
Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
'''



class Solution(object):
    def get_length(self, head):
        p = head
        l = 0
        while p is not None:
            p = p.next
            l += 1
        return l
    def get_intersection(self, headA, headB):
        if headA is None or headB is None:
            return None
        la = self.get_length(headA)
        lb = self.get_length(headB)
        p1 = headA
        p2 = headB
        if la > lb:
            p1, p2 = p2, p1
        diff = abs(la - lb)
        while diff > 0:
            p2 = p2.next
            diff -= 1
        while p1 is not None and p2 is not None:
            if p1 == p2:
                return p1
            p1 = p1.next
            p2 = p2.next
        return None