#!/usr/bin/env python2.7


'''
Write a function to find the longest common prefix string amongst an array of strings.
'''


class Solution(object):
    def helper(self, str1, str2):
        if str1 is None or str2 is None:
            return ''
        if str1 == str2:
            return str1
        s1 = str1
        s2 = str2
        if len(str1) > len(str2):
            s1, s2 = str2, str1
        ret = []
        for i in xrange(len(s1)):
            if s1[i] != s2[i]:
                break
            ret.append(s1[i])
        return ''.join(ret)

    def longest_commone_prefix(self, strs):
        if strs is None or len(strs) == 0:
            return ''
        ret = strs[0]
        i = 1
        while i < len(strs):
            ret = self.helper(ret, strs[i])
            if ret is None:
                return ''
            i += 1
        return ret

