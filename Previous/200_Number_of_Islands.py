'''
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

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

class Solution(object):
    def island(self, grid, i, j, m, n):
        grid[i][j] = '0'
        paths = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        for path in paths:
            x = i + path[0]
            y = j + path[1]
            if x >= 0 and y >= 0 and x < m and y < n and grid[x][y] == '1':
                self.island(grid, x, y, m, n)
        
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        ans = 0
        if not grid:
            return ans
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    ans += 1
                    self.island(grid, i, j, m, n)
        
        return ans