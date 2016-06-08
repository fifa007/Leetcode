#!/usr/bin/env python2.7

'''
Given two numbers represented as strings, return multiplication of the numbers as a string.

Note:
The numbers can be arbitrarily large and are non-negative.
Converting the input string to integer is NOT allowed.
You should NOT use internal library such as BigInteger.
'''


class Solution(object):
    def multiply_strings(self, nums1, nums2):
        if nums1 is None or nums2 is None:
            return None
        if nums1 == ['0'] or nums2 == ['0']:
            return '0'
        n1, n2 = len(nums1), len(nums2)
        ret = [0] * (n1 + n2)
        for i in xrange(n1-1, -1, -1):
            for j in xrange(n2-1, -1, -1):
                ret[i+j+1] = int(nums1[i]) * int(nums2[j])

        carry = 0
        for i in xrange(n1+n2-1, -1, -1):
            val = ret[i] + carry
            ret[i] = val % 10
            carry = val / 10
        if carry != 0:
            ret[0] = carry

        return ''.join([str(i) for i in ret]).lstrip('0')