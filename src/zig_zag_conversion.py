#!/usr/bin/env python2.7


'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

'''

class Solution(object):
    def conversion(self, s, numRows):
        if s is None or len(s) == 0 or numRows < 0:
            return ''
        ret_list = []
        l = [''] * numRows
        row = 0
        i = 0
        downwards = True
        while i < len(s):
            if downwards:
                l[row] = s[i]
                row += 1
                if row == numRows:
                    row -= 2
                    ret_list.append(l)
                    l = [''] * numRows
                    downwards = False
            else:
                if row > 0:
                    l[row] = s[i]
                    ret_list.append(l)
                    l = [''] * numRows
                    row -= 1
                else:
                    row = 0
                    downwards = True
                    continue
            i += 1
        ret_list.append(l)
        strs = []
        for r in xrange(numRows):
            strs.append(''.join(ret_list[c][r] for c in xrange(len(ret_list)) if ret_list[c][r] != ''))
        return ''.join(strs)