#!/usr/bin/env python2.7

'''
Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

For example,
X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
'''


class Solution(object):
    def fill(self, board, x, y, target, c):
        m = len(board)
        n = len(board[0])
        if x < 0 or x >= m or y < 0 or y >= n or board[x][y] != target:
            return
        s = [(x, y)]
        while s:
            tmp = s.pop()
            i = tmp[0]
            j = tmp[1]
            board[i][j] = c
            if i > 0 and board[i-1][j] == target:
                s.append((i-1, j))
            if i < m - 1 and board[i+1][j] == target:
                s.append((i+1, j))
            if j > 0 and board[i][j-1] == target:
                s.append((i, j-1))
            if j < n - 1 and board[i][j+1] == target:
                s.append((i, j+1))

    def fill_board(self, board, target, c):
        m = len(board)
        n = len(board[0])
        for i in xrange(m):
            self.fill(board, i, 0, target, c)
            self.fill(board, i, n-1, target, c)
        for j in xrange(n):
            self.fill(board, 0, j, target, c)
            self.fill(board, m-1, j, target, c)

    def replace(self, board, target, c):
        m = len(board)
        n = len(board[0])
        for i in xrange(m):
            for j in xrange(n):
                if board[i][j] == target:
                    board[i][j] = c

    def solve(self, board):
        if board is None or len(board) == 0:
            return
        m, n = len(board), len(board[0])
        if m < 3 or n < 3:
            return
        self.fill_board(board, 'O', 'Y')
        self.replace(board, 'O', 'X')
        self.replace(board, 'Y', 'O')
