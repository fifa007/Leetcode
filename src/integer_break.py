#!/usr/bin/env python2.7


'''
Given a positive integer n, break it into the sum of at least two positive integers
and maximize the product of those integers. Return the maximum product you can get.

For example, given n = 2, return 1 (2 = 1 + 1); given n = 10, return 36 (10 = 3 + 3 + 4).

Note: you may assume that n is not less than 2.
'''


class Solution(object):
    def integer_breaker_1(self, n):
        ret = [1] * (n+1)
        for i in xrange(1, n+1):
            for j in xrange(1, i+1):
                if i+j <= n:
                    ret[i+j] = max(max(ret[i], i)*max(ret[j], j), ret[i+j])
        return ret[n]

    def integer_breaker_2(self, n):
        if n <= 3: return n-1
        ret = [1]*(n+1)
        ret[2] = 2
        ret[3] = 3
        for i in xrange(4, n+1):
            ret[i] = max(ret[i-2]*2, ret[i-3]*3)
        return ret[n]

    def integer_breaker_3(self, n):
        if n <= 3: return n-1
        m = n % 3
        if m == 0: return pow(3, n/3)
        if m == 1: return 4 * pow(3, (n-4)/3)
        if m == 2: return 2 * pow(3, n/3)
