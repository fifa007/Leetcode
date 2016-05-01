#!/usr/bin/env python2.7

'''
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

click to show spoilers.

Have you thought about this?
Here are some good questions to ask before coding. Bonus points for you if you have already thought through this!

If the integer's last digit is 0, what should the output be? ie, cases such as 10, 100.

Did you notice that the reversed integer might overflow? Assume the input is a 32-bit integer,
then the reverse of 1000000003 overflows. How should you handle such cases?

For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
'''

INT32_MAX = 2147483647


class Solution(object):
    def reverse_integer(self, x):
        if x == 0:
            return 0
        is_negative = False
        if x < 0:
            is_negative = True
        abs_x = abs(x)
        ret = 0
        while abs_x > 0:
            ret = ret * 10 + abs_x % 10
            if ret > INT32_MAX:
                return 0
            abs_x /= 10
        return ret if is_negative is False else ret * -1
