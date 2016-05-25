#!/usr/bin/env python2.7


'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
'''


class Solution(object):
    def valid_parenthese(self, s):
        l = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                l.append(c)
            else:
                if len(l) == 0:
                    return False
                if c == ')':
                    if l[-1] != '(':
                        return False
                    l.pop()
                elif c == '}':
                    if l[-1] != '{':
                        return False
                    l.pop()
                elif c == ']':
                    if l[-1] != '[':
                        return False
                    l.pop()
                else:
                    return False
        return len(l) == 0