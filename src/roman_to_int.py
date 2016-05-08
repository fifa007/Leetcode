#!/usr/bin/env python2.7


'''
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
'''


class Solution(object):
    def roman_to_int(self, s):
        if s is None or len(s) == 0:
            return 0
        l = len(s)
        d = {}
        d['I'] = 1
        d['V'] = 5
        d['X'] = 10
        d['L'] = 50
        d['C'] = 100
        d['D'] = 500
        d['M'] = 1000
        ret = d[s[l-1]]
        i = l-2
        while i >= 0:
            if d[s[i]] < d[s[i + 1]]:
                ret -= d[s[i]]
            else:
                ret += d[s[i]]
            i -= 1
        return ret