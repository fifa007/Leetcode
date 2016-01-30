#!/usr/bin/env python2.7


'''
Given a string, determine if a permutation of the string could form a palindrome.

For example,
"code" -> False, "aab" -> True, "carerac" -> True.
'''

class Solution(object):
    def is_palindrome_permutation(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s is None:
            return False
        if len(s) == 1:
            return True
        char_set = set()
        for c in s:
            if c in char_set:
                char_set.remove(c)
            else:
                char_set.add(c)
        if len(char_set) >= 2:
            return False
        return True