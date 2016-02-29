#!/usr/bin/env python2.7


'''
Reverse bits of a given 32 bits unsigned integer.

For example, given input 43261596 (represented in binary as 00000010100101000001111010011100),
return 964176192 (represented in binary as 00111001011110000010100101000000).

Follow up:
If this function is called many times, how would you optimize it?
'''


class Solution(object):
    def reverse_bits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        i = 0
        s = ""
        while i < 32:
            s += str(n & 1)
            n >>= 1
            i += 1
        return int(s, 2)