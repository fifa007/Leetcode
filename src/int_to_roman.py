#!/usr/bin/env python2.7


'''
Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.

'''

class Solution(object):
    def int_to_roman(self, num):
        if num <= 0:
            return ""
        digits = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        roman = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
        ret = ''
        l = len(digits)
        j = l - 1
        while num > 0:
            c = num / digits[j]
            if c > 0:
              for i in xrange(c):
                  ret += roman[j]
            num %= digits[j]
            j -= 1
        return ret