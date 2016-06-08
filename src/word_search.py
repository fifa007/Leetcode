#!/usr/bin/env python2.7

'''
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell,
where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example,
Given board =

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
'''


class Solution(object):
    def helper(self, board, m, n, x, y, used, word, idx):
        if idx == len(word):
            return True
        if x < 0 or x >= m or y < 0 or y >= n:
            return False
        delta = zip([1, -1, 0, 0], [0, 0, 1, -1])
        if board[x][y] == word[idx]:
            used.add((x, y))
            for d in delta:
                if self.helper(board, m, n, x+d[0], y+d[1], used, word, idx+1):
                    return True
        return False

    def search(self, board, word):
        if board is None or len(board) == 0:
            return False
        m = len(board)
        n = len(board[0])
        used = set()
        for i in xrange(m):
            for j in xrange(n):
                if self.helper(board, m, n, i, j, used, word, 0):
                    return True
        return False
