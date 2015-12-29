#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

'''
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
'''

from collections import defaultdict


class Solution(object):
    def is_valid_anagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s is None and t is None:
            return True
        elif s is None or t is None:
            return False
        else:
            if len(s) != len(t):
                return False
            d = defaultdict(int)
            for c in s:
                d[c] += 1
            for c in t:
                if d[c] == 0:
                    return False
                d[c] -= 1
            return True