#!/usr/bin/env python2.7

'''
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

For example,

Given numerator = 1, denominator = 2, return "0.5".
Given numerator = 2, denominator = 1, return "2".
Given numerator = 2, denominator = 3, return "0.(6)".
Hint:

No scary math, just apply elementary math knowledge. Still remember how to perform a long division?
Try a long division on 4/9, the repeating part is obvious. Now try 4/333. Do you see a pattern?
Be wary of edge cases! List out as many test cases as you can think of and test your code thoroughly.

'''


class Solution(object):
    def fraction_to_decimal(self, numerator, denominator):
        if denominator == 0:
            return 'inf'
        is_negative = False
        if (numerator < 0 < denominator) or \
                (numerator > 0 > denominator):
            is_negative = True
        a = abs(numerator)
        b = abs(denominator)
        mod = []
        ret = []
        l = -1
        while True:
            ret.append(a / b)
            m = a % b
            if m == 0:
                break
            if m in mod:
                l = mod.index(m)
                break
            else:
                mod.append(m)
                a = m * 10
        if len(ret) == 1:
            s = str(ret[0])
        else:
            if l == -1:
                s = str(ret[0]) + '.' + ''.join([str(i) for i in ret[1:]])
            else:
                s = str(ret[0]) + '.' + ''.join([str(i) for i in ret[1:l+1]]) + \
                    '(' + ''.join([str(i) for i in ret[l+1:]]) + ')'
        return s if not is_negative else '-' + s