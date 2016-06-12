#!/usr/bin/env python2.7


'''
Given an array of integers, find out whether there are two distinct indices i and j in the array
such that the difference between nums[i] and nums[j] is at most t and the difference between i and j is at most k.
'''

import collections

class Solution(object):
    def contain_dupes(self, nums, k, t):
        if k < 0 or t < 0:
            return False
        m = collections.OrderedDict()
        for i in xrange(len(nums)):
            key = nums[i] / max(1, t)
            for kk in (key-1, key, key+1):
                if kk in m and abs(m[kk] - nums[i]) <= t:
                    return True
            m[key] = nums[i]
            if i >= k:
                m.popitem(last=False)
        return False