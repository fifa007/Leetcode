#!/usr/bin/env python2.7

'''
Determine whether an integer is a palindrome. Do this without extra space.
'''


class Solution(object):
    def is_palindrom_number(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        number_of_digits = 0
        while x / pow(10, number_of_digits) > 0:
            number_of_digits += 1
        while x > 0 and number_of_digits > 0:
            high_digit = x / pow(10, number_of_digits - 1)
            low_digit = x % 10
            if high_digit != low_digit:
                return False
            x = (x % pow(10, number_of_digits - 1))/10
            number_of_digits -= 2
        return True