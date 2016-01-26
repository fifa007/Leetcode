#!/usr/bin/env python2.7


'''
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to determine if a number is strobogrammatic. The number is represented as a string.

For example, the numbers "69", "88", and "818" are all strobogrammatic.
'''

class Solution(object):
    def is_strobogrammatic_number(self, num):
        """
        :type num: str
        :rtype: bool
        """
        if num < 0:
            return False
        if num <= 1:
            return True
        l = len(num)
        i = 0
        j = l - 1
        while i <= j:
            if i == j:
                if num[i] != '0' and num[i] != '1' and num[i] != '8':
                    return False
            elif num[i] == '6' or num[i] == '9':
                    k = '6' if num[i] == '9' else '9'
                    if num[j] != k:
                        return False
            elif num[i] == '0' or num[i] == '1' or num[i] == '8':
                if num[j] != num[i]:
                    return False
            else:
                return False
            i += 1
            j -= 1
        return True
