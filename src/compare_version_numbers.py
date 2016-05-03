#!/usr/bin/env python2.7

'''
Compare two version numbers version1 and version2.
If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three",
it is the fifth second-level revision of the second first-level revision.

Here is an example of version numbers ordering:

0.1 < 1.1 < 1.2 < 13.37
'''


class Solution(object):
    def compare_versions(self, version1, version2):
        strs1 = version1.split('.')
        strs2 = version2.split('.')
        i = 0
        j = 0
        while i < len(strs1) and j < len(strs2):
            if not strs1[i].isdigit() or not strs2[j].isdigit():
                return 2
            if int(strs1[i]) > int(strs2[j]):
                return 1
            elif int(strs1[i]) < int(strs2[j]):
                return -1
            i += 1
            j += 1
        while i < len(strs1):
            if int(strs1[i]) != 0:
                return 1
            i += 1
        while j < len(strs2):
            if int(strs2[j]) != 0:
                return -1
            j += 1
        return 0