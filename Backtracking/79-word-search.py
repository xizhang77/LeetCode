# -*- coding: utf-8 -*-

'''
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
'''

class Solution(object):
    def dfs(self, board, word, i, j, m, n, path ):
        if self.ans:
            return
        if not word:
            self.ans = True
            return

        dr = [ [0,1], [1,0], [-1,0], [0,-1] ]
        for d in dr:
            ii, jj  = i + d[0], j + d[1]
            if 0 <= ii < m and 0 <= jj < n and [ii,jj] not in path and board[ii][jj] == word[0]:
                self.dfs( board, word[1:], ii, jj, m, n, path + [[ii,jj]] )
            
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board or not board[0]:
            return False
        
        m, n = len(board), len(board[0])
        self.ans = False
        
        for i in range( m ):
            for j in range( n ):
                if board[i][j] == word[0]:
                    self.dfs( board, word[1:], i, j, m, n, [ [i,j] ] )
                    if self.ans:
                        return True
        
        return False