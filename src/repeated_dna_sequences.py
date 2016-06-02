#!/usr/bin/env python2.7

'''
All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T,
for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

For example,

Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",

Return:
["AAAAACCCCC", "CCCCCAAAAA"].
'''


class Solution(object):
    def find_sequences(self, s):
        if s is None:
            return []
        n = len(s)
        d = dict()
        ret = []
        for i in xrange(n-8):
            ss = s[i:i+10]
            if d.has_key(ss):
                d[ss] += 1
            else:
                d[ss] = 1

        for key, item in d.iteritems():
            if item > 1:
                ret.append(key)

        return ret