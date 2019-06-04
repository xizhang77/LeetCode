# -*- coding: utf-8 -*-

'''
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) 
connected 4-directionally (horizontal or vertical.) You may assume all four edges of 
the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island 
must be connected 4-directionally.
Example 2:

[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.
Note: The length of each dimension in the given grid does not exceed 50.
'''

# Time and Space: O(n^2)
class Solution(object):
    def dfs(self, grid, i, j, m, n):
        grid[i][j] = 0
        direct = [ [1,0], [0,1], [-1,0], [0,-1] ]
        for d in direct:
            ii, jj = i + d[0], j + d[1]
            if 0 <= ii < m and 0 <= jj < n and grid[ii][jj] == 1:
                self.count += 1
                self.dfs( grid, ii, jj, m, n )
                
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.ans = 0
        
        if not grid or not grid[0]:
            return self.ans
        
        m, n = len(grid), len(grid[0])
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.count = 1
                    self.dfs( grid, i, j, m, n )
                    self.ans = max( self.ans, self.count )
        
        return self.ans