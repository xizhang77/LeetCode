# -*- coding: utf-8 -*-
'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?


An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Note: m and n will be at most 100.

Example 1:

Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2

Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
'''


# Time & Space: O(m*n)
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid or not obstacleGrid[0]:
            return 0
        
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        dp = [ [0 for _ in range(n)] for _ in range(m) ]
        
        dp[0][0] = 1 if obstacleGrid[0][0] != 1 else 0
        
        for i in range( m ):
            for j in range( n ):
                if obstacleGrid[i][j] == 1:
                    continue
                    
                if i == 0 and j > 0 and obstacleGrid[i][j-1] != 1:
                    dp[i][j] += dp[i][j-1]
                elif j == 0 and i > 0 and obstacleGrid[i-1][j] != 1:
                    dp[i][j] += dp[i-1][j]
                elif i > 0 and j > 0:
                    if obstacleGrid[i-1][j] != 1:
                        dp[i][j] += dp[i-1][j]
                    if obstacleGrid[i][j-1] != 1:
                        dp[i][j] += dp[i][j-1]
        
        return dp[m-1][n-1]