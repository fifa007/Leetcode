#!/usr/bin/env python2.7


'''
Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".

Update (2015-02-12):
For C programmers: Try to solve it in-place in O(1) space.

click to show clarification.

Clarification:
What constitutes a word?
A sequence of non-space characters constitutes a word.
Could the input string contain leading or trailing spaces?
Yes. However, your reversed string should not contain leading or trailing spaces.
How about multiple spaces between two words?
Reduce them to a single space in the reversed string.

'''


class Solution(object):
    def reverse_words(self, s):
        ret = ''
        word = ''
        for c in s:
            if c != ' ':
                word += c
            else:
                if len(word) != 0:
                    ret = word + ' ' + ret
                    word = ''
        if len(word) != 0:
            ret = word + ' ' + ret
        return ret[0:-1]