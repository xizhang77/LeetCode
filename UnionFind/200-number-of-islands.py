# -*- coding: utf-8 -*-

'''
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
'''

# Solution 1: Recursive/DFS
class Solution(object):
    def dfs(self, grid, i, j, m, n):
        grid[i][j] = '0'
        direct = [ [1,0], [0,1], [-1,0], [0,-1] ]
        for d in direct:
            ii, jj = i + d[0], j + d[1]
            if 0 <= ii < m and 0 <= jj < n and grid[ii][jj] == '1':
                self.dfs( grid, ii, jj, m, n )
                
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0
        
        if not grid or not grid[0]:
            return count
        
        m, n = len(grid), len(grid[0])
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    self.dfs( grid, i, j, m, n )
        
        return count


# Solution 2: Union Find
class Solution(object):
    def find(self, x):
        while x != self.parent[ x ]:
            x = self.parent[ x ]
        
        return x
        
    def union(self, x, y):
        pX, pY = self.find(x), self.find(y)
        if pX == pY:
            return
        self.parent[ pY ] = pX
        self.count -= 1
        
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        
        m, n = len(grid), len(grid[0])
        
        self.count = 0
        self.parent = [ i for i in range(m * n)]
        
        for i in range(m):
            for j in range(n):
                idx = i*n + j
                if grid[i][j] == '1':
                    self.count += 1
                    if j + 1 < n and grid[i][j+1] == '1':
                        self.union( idx, idx + 1 )
                    if i + 1 < m and grid[i+1][j] == '1':
                        self.union( idx, idx + n )
        
        return self.count