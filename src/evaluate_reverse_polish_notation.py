#!/usr/bin/env python2.7


'''
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:
  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
'''


class Solution(object):
    def check_int(self, s):
        if s[0] in ('+', '-'):
            return s[1:].isdigit()
        return s.isdigit()

    def operator(self, op, a, b):
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b
        elif op == '/':
            if b == 0:
                return None
            if (a > 0 and b > 0) or (a < 0 and b < 0):
                return abs(a) / abs(b)
            else:
                return -(abs(a) / abs(b))

    def calculate(self, tokens):
        if tokens is None:
            return None
        n = len(tokens)
        stack = []
        for i in xrange(n):
            if self.check_int(tokens[i]):
                stack.append(int(tokens[i]))
            else:
                if len(stack) < 2:
                    return None
                right = stack[-1]
                left = stack[-2]
                stack = stack[:-2]
                stack.append(self.operator(tokens[i], left, right))
        return stack[0] if len(stack) == 1 else None