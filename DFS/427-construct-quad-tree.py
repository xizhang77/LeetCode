# -*- coding: utf-8 -*-

'''
https://leetcode.com/problems/construct-quad-tree/
'''


"""
# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
class Solution(object):
    def dfs(self, grid, row, col):
        count = 0
        total = (row[1]-row[0])*(col[1]-col[0])
        
        for i in range(row[0], row[1]):
            for j in range(col[0], col[1]):
                count = count + 1 if grid[i][j] == 1 else count
        
        
        val = True if count == total else False
        isLeaf = True if (count == total or count == 0) else False
                
        root = Node( None )
        root.isLeaf = isLeaf
        root.val = val
                
        if isLeaf == False:
            midRow = (row[0]+row[1])/2
            midCol = (col[0]+col[1])/2
            root.topLeft = self.dfs( grid, [row[0], midRow], [col[0], midCol])
            root.topRight = self.dfs( grid, [row[0], midRow], [midCol, col[1]])
            root.bottomLeft = self.dfs( grid, [midRow, row[1]], [col[0], midCol])
            root.bottomRight = self.dfs( grid, [midRow, row[1]], [midCol, col[1]])
        
        return root
    
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        if not grid or not grid[0]:
            return None
        
        n = len(grid)
        
        return self.dfs( grid, [0, n], [0, n] )