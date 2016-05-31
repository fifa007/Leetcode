#!/usr/bin/env python2.7


'''
Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:
For the return value, each inner list's elements must follow the lexicographic order.
All inputs will be in lower-case.
'''

class Solution(object):
    def group_anagrams(self, strs):
        if strs is None or len(strs) == 0:
            return []
        strs.sort()
        n = len(strs)
        d = dict()
        for i in xrange(n):
            k = ''.join(sorted(strs[i]))
            if d.has_key(k):
                d[k].append(strs[i])
            else:
                d[k] = [strs[i]]
        ret = []
        for _, values in d.iteritems():
            ret.append(values)
        return ret