#!/usr/bin/env python2.7

'''
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring,
"pwke" is a subsequence and not a substring.
'''

class Solution(object):
    def longest_substring(self, s):
        if s is None:
            return 0
        n = len(s)
        length = 0
        i = 0
        j = 0
        m = dict()
        while j < n:
            if s[j] not in m:
                m[s[j]] = j
            else:
                length = max(length, j-i)
                if i < m[s[j]] + 1:
                    i = m[s[j]] + 1
                m[s[j]] = j
            j += 1
        length = max(length, j-i)
        return length