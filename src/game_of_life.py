#!/usr/bin/env python2.7

'''
According to the Wikipedia's article: "The Game of Life, also known simply as Life,
is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0).
Each cell interacts with its eight neighbors (horizontal, vertical, diagonal)
using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state.

Follow up:
Could you solve it in-place? Remember that the board needs to be updated at the same time:
You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite,
which would cause problems when the active area encroaches the border of the array.
How would you address these problems?
'''

class Solution(object):
    def get_lives(self, board, x, y):
        ret = 0
        for i in xrange(x-1, x+2):
            for j in xrange(y-1, y+2):
                if i < 0 or y < 0 or i > len(board)-1 or y > len(board[0])-1 or (i==x and j==y):
                    continue
                ret += board[i][j] & 1

    def game_of_life(self, board):
        if board is None or len(board) == 0 or len(board[0]) == 0:
            return
        m = len(board)
        n = len(board[0])
        for i in xrange(m):
            for j in xrange(n):
                c = self.get_lives(board, i, j)
                if board[i][j] and (c == 2 or c == 3):
                    board[i][j] |= 2
                elif not board[i][j] and c == 3:
                    board[i][j] |= 2

        for i in xrange(m):
            for j in xrange(n):
                board[i][j] >>= 1