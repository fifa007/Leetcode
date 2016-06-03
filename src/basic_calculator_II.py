#!/usr/bin/env python2.7


'''
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces.
The integer division should truncate toward zero.

You may assume that the given expression is always valid.

Some examples:
"3+2*2" = 7
" 3/2 " = 1
" 3+5 / 2 " = 5
Note: Do not use the eval built-in library function.
'''

import re
import operator

class Solution(object):
    def calculate(self, s):
        s1 = re.sub(r'\d+', ' \g<0> ', s)
        expression = s1.split()
        total = d = 0
        idx = 0
        op = {'+': operator.add, '-': operator.sub, \
              '*': operator.mul, '/': operator.floordiv}
        func = op['+']
        while idx < len(expression):
            e = expression[idx]
            if e in '+-':
                total = func(total, d)
                func = op[e]
            elif e in '*/':
                idx += 1
                d = op[e](d, int(expression[idx]))
            else:
                d = int(e)
            idx += 1
        return func(total, d)