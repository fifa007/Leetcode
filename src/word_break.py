#!/usr/bin/env python2.7

'''
Given a string s and a dictionary of words dict, determine
if s can be segmented into a space-separated sequence of one or more dictionary words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".
'''


class Solution(object):
    def word_break(self, s, wordDict):
        if s is None:
            return False
        n = len(s)
        dp = [False] * (n+1)
        dp[n] = True
        for i in xrange(n-1, -1, -1):
            for j in xrange(i, n):
                if s[i:j+1] in wordDict and dp[j+1]:
                    dp[i] = True
                    break
        return dp[0]