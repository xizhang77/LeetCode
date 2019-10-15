# -*- coding: utf-8 -*-

'''
https://leetcode.com/problems/design-tic-tac-toe/
'''

# Time: O(1) per move() function
# Spce: O(n)
from collections import defaultdict
class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.n = n
        self.board = {}
        
        self.board['row'] = defaultdict( int )
        self.board['col'] = defaultdict( int )
        self.board['diag1'] = 0
        self.board['diag2'] = 0

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        self.board['row'][ row ] += 1 if player == 1 else -1
        self.board['col'][ col ] += 1 if player == 1 else -1
        
        if abs(self.board['row'][row]) == self.n:
            return 1 if self.board['row'][row] > 0 else 2
        if abs(self.board['col'][col]) == self.n:
            return 1 if self.board['col'][col] > 0 else 2
        
        if row == col:
            self.board['diag1'] += 1 if player == 1 else -1
        if row + col == self.n - 1:
            self.board['diag2'] += 1 if player == 1 else -1
        
        if abs(self.board['diag1']) == self.n:
            return 1 if self.board['diag1'] > 0 else 2
        if abs(self.board['diag2']) == self.n:
            return 1 if self.board['diag2'] > 0 else 2
        
        
        return 0
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)