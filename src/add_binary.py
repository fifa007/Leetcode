#!/usr/bin/env python2.7


'''
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
'''


class Solution(object):
    def add_binary(self, a, b):
        if a is None or b is None:
            return ''
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        ret = []
        while i >= 0 and j >= 0:
            tmp = int(a[i]) + int(b[j]) + carry
            ret.insert(0, str(tmp % 2))
            carry = tmp / 2
            i -= 1
            j -= 1
        while i >= 0:
            tmp = int(a[i]) + carry
            ret.insert(0, str(tmp % 2))
            carry = tmp / 2
            i -= 1
        while j >= 0:
            tmp = int(b[j]) + carry
            ret.insert(0, str(tmp % 2))
            carry = tmp / 2
            j -= 1
        if carry == 1:
            ret.insert(0, str(carry))
        return ''.join(ret)