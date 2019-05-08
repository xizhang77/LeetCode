# -*- coding: utf-8 -*-

'''
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
'''

# Time: O(m*n); Space: O(1) [No extra space needed]
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        
        m, n = len(grid), len(grid[0])
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                if i == 0 and j > 0:
                    grid[0][j] += grid[0][j-1]
                elif j == 0 and i > 0:
                    grid[i][0] += grid[i-1][0]
                else:
                    grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        
        return grid[m-1][n-1]