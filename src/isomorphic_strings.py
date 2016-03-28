#!/usr/bin/env python2.7


'''
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character
while preserving the order of characters.
No two characters may map to the same character but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.

Note:
You may assume both s and t have the same length.


'''


class Solution(object):
    def is_isomorphic_strings(self, s, t):
        """

        :param s: string
        :param t: string
        :return: boolean
        """
        if s is None or t is None:
            return s == t
        if len(s) != len(t):
            return False
        i = 0
        dict = {}
        while i < len(s):
            if s[i] in dict:
                if t[i] != dict[s[i]]:
                    return False
            else:
                if t[i] in dict.itervalues():
                    return False
                dict[s[i]] = t[i]
            i += 1
        return True