#!/usr/bin/env python2.7

'''

'''

import math

class Solution(object):
    def get_primes(self, n):
        if n <= 1:
            return []
        factors = []
        d = 2
        while n > 1:
            while n % d == 0:
                factors.append(d)
                n /= d
            d += 1
            if d * d > n:
                if n > 1:
                    factors.append(n)
                    break
        return factors

    def super_ugly_number(self, n, primes):
        if n <= 0:
            return None
        if n == 1:
            return 1
        p = self.super_ugly_number(n-1, primes)
        i = p + 1
        while True:
            curr_primes = self.get_primes(i)
            if set(curr_primes) <= set(primes):
                return i
            i += 1

