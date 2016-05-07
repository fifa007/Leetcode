#!/usr/bin/env python2.7


'''
Given a string array words, find the maximum value of length(word[i]) * length(word[j])
where the two words do not share common letters. You may assume that each word will contain only lower case letters.
If no such two words exist, return 0.

Example 1:
Given ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
Return 16
The two words can be "abcw", "xtfn".

Example 2:
Given ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
Return 4
The two words can be "ab", "cd".

Example 3:
Given ["a", "aa", "aaa", "aaaa"]
Return 0
No such pair of words.
'''


class Solution(object):
    def max_product(self, words):
        if words is None or len(words) == 0:
            return 0
        l = len(words)
        ret = 0
        element = [0] * l
        for i in xrange(l):
            for c in words[i]:
                element[i] |= 1 << (ord(c) - 97)

        for i in xrange(l):
            for j in xrange(i+1, l):
                if element[i] & element[j] == 0:
                    ret = max(ret, len(words[i]) * len(words[j]))

        return ret