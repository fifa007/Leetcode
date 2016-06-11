#!/usr/bin/env python2.7

'''
Given two words (beginWord and endWord), and a dictionary's word list,
find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the word list
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Note:
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
'''


class Solution(object):
    def ladder_length(self, begin, end, word_dict):
        if begin == end:
            return 0
        q = [(begin, 1)]
        word_dict.add(end)
        while q:
            tmp = q.pop(0)
            curr = tmp[0]
            curr_len = tmp[1]
            if curr == end:
                return curr_len
            for i in xrange(len(begin)):
                p1 = curr[:i]
                p2 = curr[i+1:]
                for j in xrange(26):
                    c = chr(j + ord('a'))
                    if c == curr[i]: continue
                    s = p1 + c + p2
                    if s in word_dict:
                        q.append((s, curr_len + 1))
                        word_dict.remove(s)
        return 0