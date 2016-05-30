#!/usr/bin/env python2.7

'''
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Example 1:

11110
11010
11000
00000
Answer: 1

Example 2:

11000
11000
00100
00011
Answer: 3
'''


class Solution(object):
    def number_of_islandes(self, grid):
        if grid is None or len(grid) == 0:
            return 0
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for i in xrange(m)]
        ret = 0
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    ret += 1
                    self.visit(grid, m, n, visited, i, j)
        return ret

    def visit(self, grid, m, n, visited, x, y):
        q = [(x, y)]
        visited[x][y] = True
        dz = zip([1, -1, 0, 0], [0, 0, 1, -1])
        while q:
            tmp = q.pop(0)
            for d in dz:
                p = (tmp[0] + d[0], tmp[1] + d[1])
                if self.is_valid(p) and grid[p[0]][p[1]] == '1' and not visited[p[0]][p[1]]:
                    visited[p[0]][p[1]] = True
                    q.append(p)

    def is_valid(self, m, n, p):
        return p[0] >= 0 and p[0] < m and p[1] >= 0 and p[1] < n