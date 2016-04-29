#!/usr/bin/env python2.7

'''
Description:

Count the number of prime numbers less than a non-negative number, n.
'''

import math

class Solution(object):
    def count_primes(self, n):
        if n < 0:
            return -1
        candidates = [True for i in range(2, n)]
        candidates.insert(0, False)
        candidates.insert(0, False)
        i = 2
        while i <= math.sqrt(n):
            if candidates[i]:
                j = i * i
                while j < n:
                    candidates[j] = False
                    j += i
            i += 1
        return sum([1 for c in candidates if c == True])