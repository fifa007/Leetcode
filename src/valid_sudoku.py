#!/usr/bin/env python2.7

'''
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

A partially filled sudoku which is valid.

Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.
'''


class Solutiion(object):
    def is_valid_vector(self, aList):
        item_set = set()
        for index in range(len(aList)):
            if aList[index] == '.':
                continue
            if len(aList[index]) != 1:
                return False
            value = ord(aList[index]) - ord('0')
            if value in item_set:
                return False
            item_set.add(value)
        return True

    def is_valid_suduko(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        if board is None:
            return False
        for row in range(len(board)):
            if self.is_valid_vector(row) is False:
                return False
        for col in range(len(board[0])):
            v = [row[col] for row in board]
            if self.is_valid_vector(v) is False:
                return False
        i = 0
        while i < 9:
            j = 0
            while j < 9:
                v = []
                for k in range(i, i + 3):
                    for l in range(j, j + 3):
                        v.append(board[k][l])
                if self.is_valid_vector(v) is False:
                    return False
                j = j + 3
            i = i + 3
        return True