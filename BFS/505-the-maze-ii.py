# -*- coding: utf-8 -*-

'''
https://leetcode.com/problems/the-maze-ii/
'''

# Solution 1: BFS
# Time & Space: O(mn)
class Solution(object):

    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        if not maze or not maze[0]:
            return -1
        m, n = len( maze ), len( maze[0] )
        
        dp = [ [ float('inf') ]*n for _ in range( m ) ]
        dp[ start[0] ][ start[1] ] = 0
        
        queue = [ start ]
        direct = [ [0,1], [1,0], [-1,0], [0,-1] ]
        
        while queue:
            i, j = queue.pop( 0 )
            for d in direct:
                ii, jj = i, j
                count = dp[i][j]
                while 0 <= ii + d[0] < m and 0 <= jj + d[1] < n and maze[ii+d[0]][jj+d[1]] == 0:
                    ii += d[0]
                    jj += d[1]
                    count += 1
                if dp[ii][jj] > count:
                    dp[ii][jj] = count
                    queue.append( [ii,jj] )
        return dp[destination[0]][destination[1]] if dp[destination[0]][destination[1]] != float('inf') else -1
                