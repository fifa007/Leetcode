#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

'''
Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = “coding”, word2 = “practice”, return 3.
Given word1 = "makes", word2 = "coding", return 1.

Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.
'''


import sys

class Solution(object):
    def shortest_distance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if words is None or len(words) < 2:
            return -1
        if word1 not in words or word2 not in words:
            return -1
        ret = sys.maxint
        idx1 = -1
        idx2 = -1
        for i, w in enumerate(words):
            if w != word1 and w != word2:
                continue
            if w == word1:
                idx1 = i
            if w == word2:
                idx2 = i
            if idx1 != -1 and idx2 != -1:
                ret = min(ret, abs(idx1 - idx2))
        return ret
