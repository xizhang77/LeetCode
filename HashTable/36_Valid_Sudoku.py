# -*- coding: utf-8 -*-

'''
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

A partially filled sudoku which is valid.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

Example 1:

Input:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: true
Example 2:

Input:
[
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being 
    modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
The given board contain only digits 1-9 and the character '.'.
The given board size is always 9x9.
'''


# Solution 1: Time: O(n^2); Space: O(9)
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        n = len(board)
        
        # Row
        for i in range( n ):
            temp = [ x for x in board[i] if x != '.' ]
            if len( temp ) != len( set(temp) ):
                return False
        
        # Col
        for j in range( n ):
            temp = [ board[i][j] for i in range(n) if board[i][j] != '.' ]
            if len( temp ) != len( set(temp) ):
                return False
            
        # Box
        for j in range(0, n, 3):
            temp = []
            for i in range(n):
                temp += [ board[i][j+k] for k in range(3) if board[i][j+k] != '.']
                if (i+1)%3 == 0:
                    if len( temp ) != len( set(temp) ):
                        return False
                    temp = []
            
        return True

# Solution 2: Much simpler version; Time: O(n^2) Space: O(n^2)
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        check = set()
        
        n = len(board)
        
        for i in range( n ):
            for j in range( n ):
                if board[i][j] != '.':
                    if (i, board[i][j]) in check or (board[i][j], j) in check or (i/3, j/3, board[i][j]) in check:
                        return False
                    check.add( (i, board[i][j]) )
                    check.add( (board[i][j], j) )
                    check.add( (i/3, j/3, board[i][j]) )
        
        return True