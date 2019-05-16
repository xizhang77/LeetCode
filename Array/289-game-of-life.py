# -*- coding: utf-8 -*-

'''
According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.

Example:

Input: 
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Output: 
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]
Follow up:

Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?
'''

# Time & Space: O(mn)
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        modify = []
        
        m, n = len(board), len(board[0])
        
        hashMap = {}
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 1:
                    if i in hashMap:
                        hashMap[i] += [j]
                    else:
                        hashMap[i] = [j]
        
        check = {-1:[-1,0,1], 0:[-1,1], 1:[-1,0,1]}
        for i in range(m):
            for j in range(n):
                count = 0
                for key in check:
                    if i + key in hashMap:
                        count += sum( [1 for val in check[key] if j + val in hashMap[ i + key ]])
                if (count < 2 or count > 3) and board[i][j] == 1:
                    modify.append([i,j, 0])
                elif count == 3 and board[i][j] == 0:
                    modify.append([i,j, 1])
        
        for item in modify:
            i, j, val = item
            board[i][j] = val

# Solution 2: Modify in-place [Also satify the follow up quesiton]
# Refer: https://leetcode.com/problems/game-of-life/solution/
# When follow the 1st rule ( board[i][j] == 1 and count<2 or >3, board[i][j] = 2)
# When follow the 2nd rule ( board[i][j] == 0 and count==3, board[i][j] = -1)
# Finally modify the cells with 2 or -1
