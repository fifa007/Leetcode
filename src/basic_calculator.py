#!/usr/bin/env python2.7

'''
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ),
the plus + or minus sign -, non-negative integers and empty spaces .

You may assume that the given expression is always valid.

Some examples:
"1 + 1" = 2
" 2-1 + 2 " = 3
"(1+(4+5+2)-3)+(6+8)" = 23
Note: Do not use the eval built-in library function.
'''


class Solution(object):
    def caculate(self, s):
        if s is None:
            return 0
        sign = [1, 1]
        ret = 0
        i = 0
        while i < len(s):
            if s[i].isdigit():
                num = int(s[i])
                j = i + 1
                while j < len(s) and s[j].isdigit():
                    num = num*10 + int(s[j])
                    j += 1
                i = j - 1
                ret += sign[-1] * num
                sign.pop()
            elif s[i] == ')':
                sign.pop()
            elif s[i] != ' ':
                c = -1 if s[i] == '-' else 1
                sign.append(sign[-1] * c)
            i += 1
        return ret