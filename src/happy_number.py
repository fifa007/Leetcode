#!/usr/bin/env python2.7


'''
Write an algorithm to determine if a number is "happy".
A happy number is a number defined by the following process:
Starting with any positive integer, replace the number by the sum of the squares of its digits,
and repeat the process until the number equals 1 (where it will stay),
or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy numbers.
Example: 19 is a happy number

12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
'''


def get_digits(n):
    ret = []
    while n:
        ret.insert(0, n % 10)
        n /= 10
    return ret


def caculate_square(nums):
    ret = 0
    for num in nums:
        ret += num * num
    return ret


class Solution(object):
    def is_happy_number(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        curr_sum = n
        while curr_sum != 1:
            digits = get_digits(curr_sum)
            curr_sum = caculate_square(digits)
            if curr_sum < 10:
                break
        if curr_sum == 1:
            return True
        return False

