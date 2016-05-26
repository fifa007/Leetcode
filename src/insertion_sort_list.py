#!/usr/bin/env python2.7

'''
Sort a linked list using insertion sort.
'''

import src.data_structure

class Solution(object):
    def insert(self, head, node):
        while head.next and head.next.val <= node.val:
            head = head.next
        head.next = node.next
        node.next = head

    def insertion_sort_list(self, head):
        if head is None or head.next is None:
            return head
        ret = [src.data_structure.list_node(head.val)]
        while head.next:
            ret.append(src.data_structure.list_node(head.next.val))
            head = head.next

        ret.sort(key = lambda src.data_structure.list_node: src.data_structure.list_node.get_data())
        i = 0
        while i + 1 < len(ret):
            ret[i].next = ret[i+1]
            i += 1
        return ret[0]