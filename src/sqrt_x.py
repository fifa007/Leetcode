#!/usr/bin/env python2.7

'''
Implement int sqrt(int x).

Compute and return the square root of x.
'''


class Solution(object):
    def sqrt_x(self, x):
        if x == 0 or x == 1:
            return x
        lo = 0
        hi = x-1
        while lo <= hi:
            mid = lo + (hi-lo)/2
            val = (mid+1) * (mid+1)
            if val == x:
                return mid+1
            elif val < x:
                lo = mid + 1
            else:
                hi = mid - 1
        return lo