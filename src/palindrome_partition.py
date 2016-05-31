#!/usr/bin/env python2.7


'''
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

  [
    ["aa","b"],
    ["a","a","b"]
  ]
'''


class Solution(object):
    def partition(self, s):
        if s is None or len(s) == 0:
            return []
        n = len(s)
        dp = [[False] * n for i in xrange(n)]
        for i in xrange(n):
            dp[i][i] = True
            if i < n-1:
                dp[i][i+1] = s[i] == s[i+1]
        for i in xrange(n-3, -1, -1):
            j = i+2
            while j < n:
                dp[i][j] = dp[i+1][j-1] and s[i] == s[j]
                j += 1
        ret = []
        sol = []
        self.helper(s, dp, 0, sol, ret)
        return ret

    def helper(self, s, dictionary, start, sol, ret):
        n = len(s)
        if start == n:
            ret.append(sol)
            return
        for i in xrange(start, n):
            if dictionary[start][i]:
                tmp = sol[:]
                tmp.append(s[start:i+1])
                self.helper(s, dictionary, i+1, sol, ret)
