#!/usr/bin/env python2.7

'''
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.
'''

class Solution(object):
    def num_decodings(self, s):
        if s is None or s == '':
            return 0
        n = len(s)
        dp = [0] * (n+1)
        dp[n] = 1
        dp[n-1] = 1 if str(s[n]) >= 1 and str(s[n]) <= 9 else 0
        for i in xrange(n-2, -1, -1):
            if s[i] == '0':
                continue
            val = int(s[i:i+2])
            if val >= 1 and val <= 26:
                dp[i] = dp[i+1] + dp[i+2]
            else:
                dp[i] = dp[i+1]

        return dp[0]