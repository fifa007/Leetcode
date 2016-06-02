#!/usr/bin/env python2.7


'''
The set [1,2,3,…,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note: Given n will be between 1 and 9 inclusive.
'''


class Solution(object):
    def next_permutation(self, n, k):
        ret = []
        factorial = [1] * n
        num = []
        for i in xrange(1, n):
            factorial[i] = factorial[i-1] * i

        for i in xrange(n):
            num.append(str(i+1))

        k -= 1
        for i in xrange(n, 0, -1):
            j = k / factorial[i-1]
            k %= factorial[i-1]
            ret.append(num[j])
            del num[j]

        return ''.join(ret)