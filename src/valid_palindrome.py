#!/usr/bin/env python2.7

'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.
'''


class Solution(object):
    def is_palindrome(self, s):
        if s is None:
            return False
        if len(s) == 0:
            return True
        i = 0
        j = len(s) - 1
        while i < j:
            while i < len(s) and s[i].isalnum() == False:
                i += 1
            while j >= 0 and s[j].isalnum() == False:
                j -= 1
            if i == len(s) and j == -1:
                return True
            elif i == len(s) or j == -1:
                return False
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True