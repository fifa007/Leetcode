#!/usr/bin/env python2.7

'''
Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
'''


class Solution(object):
    def simplify_path(self, path):
        strs = path.split('/')
        ret = []
        for s in strs:
            if s:
                if s == '..':
                    if len(ret) > 0:
                        ret.pop()
                elif s != '.':
                    ret.append(s)
        return '/' + '/'.join(ret)