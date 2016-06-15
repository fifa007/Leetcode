#!/usr/bin/env python2.7

'''
Additive number is a string whose digits can form additive sequence.

A valid additive sequence should contain at least three numbers.
Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.

For example:
"112358" is an additive number because the digits can form an additive sequence: 1, 1, 2, 3, 5, 8.

1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
"199100199" is also an additive number, the additive sequence is: 1, 99, 100, 199.
1 + 99 = 100, 99 + 100 = 199
Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.

Given a string containing only digits '0'-'9', write a function to determine if it's an additive number.

Follow up:
How would you handle overflow for very large input integers?
'''


class Solution(object):
    def additive_number(self, num):
        if num is None or len(num) == 0:
            return False
        n = len(num)
        for i in xrange(1, n):
            for j in xrange(i+1, n):
                s1 = num[:i]
                s2 = num[i:j]
                if (len(s1) > 1 and s1[0] == '0') or (len(s2) > 1 and s2[0] == '0'):
                    continue
                a, b = int(s1), int(s2)
                c = a + b
                curr = s1 + s2 + str(c)
                while len(curr) < n:
                    a = b
                    b = c
                    c = a + b
                    curr += str(c)
                if curr == num:
                    return True
        return False