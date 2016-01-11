#!/usr/bin/env python2.7


'''
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
'''


class Soluttion(object):
    def roman_to_integer(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None or len(s) == 0:
            return 0
        dict = {}
        dict['I'] = 1
        dict['V'] = 5
        dict['X'] = 10
        dict['L'] = 50
        dict['C'] = 100
        dict['D'] = 500
        dict['M'] = 1000
        dict['IV'] = 4
        dict['IX'] = 9
        dict['XL'] = 40
        dict['XC'] = 90
        dict['CD'] = 400
        dict['CM'] = 900
        ret = 0
        i = 0
        while i < len(s):
            if dict.has_key(s[i:i+2]):
                ret += dict[s[i:i+2]]
                i += 2
            else:
                ret += dict[s[i]]
                i += 1
        return ret