#!/usr/bin/env python2.7


'''
Implement pow(x, n).
'''

class Solution(object):
    def pow(self, x, n):
        if n == 0:
            return 1
        fraction = False
        if n < 0:
            fraction = True
            n = -n
        ret = 0
        if n % 2 == 0:
            ret = self.pow(x*x, n/2)
        else:
            ret = self.pow(x*x, n/2) * x
        return ret if not fraction else 1/ret