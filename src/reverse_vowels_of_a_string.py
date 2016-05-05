#!/usr/bin/env python2.7

'''
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".
'''


class Solution(object):
    def is_vow(self, s):
        return s in ['a', 'e', 'i', 'o', 'u']

    def reverse_vowels(self, s):
        if s is None or len(s) == 0:
            return ''
        i = 0
        j = len(s) - 1
        ret = list(s)
        while i < j:
            if self.is_vow(s[i].lower()) and self.is_vow(s[j].lower()):
                ret[i], ret[j] = ret[j], ret[i]
            elif self.is_vow(s[i].lower()):
                j -= 1
                continue
            elif self.is_vow(s[j].lower()):
                i += 1
                continue
            i += 1
            j -= 1
        return ''.join(ret)