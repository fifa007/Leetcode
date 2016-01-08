#!/usr/bin/env python2.7

'''
Related to question Excel Sheet Column Title

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
'''


class Solution(object):
    def title_to_number_recursive(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None or len(s) == 0:
            return 0
        if len(s) == 1:
            return ord(s[0]) - ord('A') + 1
        return self.title_to_number_recursive(s[0]) * pow(26, len(s) - 1) \
                + self.title_to_number_recursive(s[1:])

    def title_to_number_iterative(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None or len(s) == 0:
            return 0
        l = len(s)
        ret = 0
        for c in s:
            d = ord(c) - ord('A') + 1
            ret += d * pow(26, l - 1)
            l = l - 1
        return ret