# -*- coding: utf-8 -*-

'''
https://leetcode.com/problems/number-of-distinct-islands/
'''

# Time and Space: O(n^2)
class Solution(object):
    def dfs(self, grid, x, y, i, j, path):
        grid[i][j] = 0
        
        direct = [ [0,1], [1,0], [0,-1], [-1,0] ]
        for d in direct:
            ii, jj = i + d[0], j + d[1]
            if 0 <= ii < len(grid) and 0 <= jj < len(grid[0]) and grid[ii][jj] == 1:
                path.append( (ii-x, jj-y) )
                self.dfs( grid, x, y, ii, jj, path)
                
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        
        check = []
        
        for i in range( len(grid) ):
            for j in range( len(grid[0]) ):
                if grid[i][j] == 1:
                    path = [ (0,0) ]
                    self.dfs( grid, i, j, i, j, path )
                    path = sorted( path )
                    # print path
                    if path not in check:
                        check.append( path )
        
        
        return len(check)