#!/usr/bin/env python2.7


'''
Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".
'''


class Solution(object):
    def reverse_string(self, s):
        if s is None:
            return None
        i = len(s) - 1
        j = 0
        ret = list("a" * len(s))
        while i >= 0:
            ret[j] = s[i]
            i -= 1
            j += 1
        return ''.join(ret)