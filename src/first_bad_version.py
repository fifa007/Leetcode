#!/usr/bin/env python2.7

'''
You are a product manager and currently leading a team to develop a new product. Unfortunately,
the latest version of your product fails the quality check. Since each version is developed based
on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one,
which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad.
Implement a function to find the first bad version. You should minimize the number of calls to the API.

'''


def IsBadVersion(x):
    return x < 0


class Solution(object):
    def helper(self, start, end):
        if start > end:
            return -1
        if start == end:
            if IsBadVersion(start):
                return start
            return -1
        mid = start + (end - start) / 2
        if IsBadVersion(mid):
            ret = self.helper(start, mid - 1)
            if ret == -1:
                return mid
            return ret
        else:
            return self.helper(mid + 1, end)

    def get_first_bad_version(self, n):
        if n <= 0:
            return -1
        return self.helper(1, n)