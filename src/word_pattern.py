#!/usr/bin/env python2.7


'''
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Examples:
pattern = "abba", str = "dog cat cat dog" should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog" should return false.
pattern = "abba", str = "dog dog dog dog" should return false.
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.
'''


class Solution(object):
    def word_patter(self, pattern, str):
        if pattern is None or str is None:
            return False
        strs = str.split(' ')
        if len(pattern) != len(strs):
            return False
        d = {}
        s = set()
        for i in xrange(len(pattern)):
            if d.has_key(pattern[i]):
                if d[pattern[i]] != strs[i]:
                    return False
            else:
                if strs[i] in s:
                    return False
                d[pattern[i]] = strs[i]
                s.add(strs[i])
        return True