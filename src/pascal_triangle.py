#!/usr/bin/env python2.7

'''
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''


class Solution(object):
    def generate_pascal_triangle(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows <= 0:
            return []
        ret = []
        if numRows == 1:
            ret = [[1]]
        if numRows >= 2:
            ret = [[1], [1, 1]]
        i = 3
        prev_row = [1, 1]
        while i <= numRows:
            curr_row = [1]
            for j in range(len(prev_row) - 1):
                curr_row.append(prev_row[j] + prev_row[j + 1])
            curr_row.append(1)
            ret.append(curr_row)
            prev_row = curr_row
            i += 1
        return ret