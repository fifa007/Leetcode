#!/usr/bin/env python2.7


'''

'''

INT32_MAX = pow(2, 31) - 1

class Solution(object):
    def convert_str_to_int(self, s):
        if s is None or len(s) == 0 or s[1:].isdigit() == False:
            return 0
        is_negative = False
        i = 0
        ret = 0
        if s[0] == '+' or s[0] == '-':
            is_negative = s[0] == '-'
            i = 1
        while i < len(s) and s[i].isdigit() == False:
            i += 1
        if i == len(s):
            return 0
        while i < len(s):
            if s[i].isdigit() == False:
                break
            else:
                ret = ret * 10 + int(s[i])
                if is_negative is False and ret > INT32_MAX:
                    ret = INT32_MAX
                    break
                if is_negative is True and ret > INT32_MAX + 1:
                    ret = INT32_MAX + 1
                    break
            i += 1
        return ret if is_negative is False else -ret

