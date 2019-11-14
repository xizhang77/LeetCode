# -*- coding: utf-8 -*-

'''
https://leetcode.com/problems/minesweeper/
'''
class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board
        
        m, n = len(board), len(board[0])
        curr = [ click ]
        
        direct = [[1,0],[0,1],[-1,0],[0,-1],[1,1],[1,-1],[-1,1],[-1,-1]]
        
        while curr:
            nxt = set()
            for node in curr:
                i, j = node 
                count = 0
                temp = []
                for d in direct:
                    ii, jj = i + d[0], j + d[1]
                    if 0 <= ii < m and 0 <= jj < n:
                        if board[ii][jj] == 'E':
                            temp.append( (ii,jj) )
                        elif board[ii][jj] == 'M':
                            count += 1
                if count:
                    board[i][j] = str( count )
                else:
                    board[i][j] = 'B'
                    nxt |= set( temp )
            curr = list(nxt)
        
        return board
                
                        