# -*- coding: utf-8 -*-

'''
https://leetcode.com/problems/island-perimeter/
'''

# Solution 1: Brute-Force...
# Time: O(4*m*n)

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        
        ans = 0
        
        m, n = len(grid), len(grid[0])
        direct = [ [1,0], [0,1], [-1,0], [0,-1] ]
        
        for i in range( m ):
            for j in range( n ):
                if grid[i][j] == 1:
                    count = 4
                    for d in direct:
                        ii, jj = i + d[0], j + d[1]
                        if 0 <= ii < m and 0 <= jj < n and grid[ii][jj]:
                            count -= 1
                    ans += count
        
        return ans