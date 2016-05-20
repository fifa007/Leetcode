#!/usr/bin/env python2.7

'''
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

Note that 1 is typically treated as an ugly number.

Show Hint

'''

class Solution(object):
    def nth_ugly_number(self, n):
        if n <= 0:
            return None
        ret = [1]
        i = j = k = 0
        while len(ret) < n:
            num = min(ret[i]*2, min(ret[j]*3, ret[k]*5))
            ret.append(num)
            if num % 2 == 0:
                i += 1
            if num % 3 == 0:
                j += 1
            if num % 5 == 0:
                k += 1
        return ret[len(ret)-1]