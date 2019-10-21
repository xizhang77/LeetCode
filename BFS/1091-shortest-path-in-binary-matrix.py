# -*- coding: utf-8 -*-

'''
https://leetcode.com/problems/shortest-path-in-binary-matrix/
'''

class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        
        n = len( grid )
        
        ans = 1
        curr = [ [0,0] ]
        grid[0][0] = 1
        direct = [ [1,0], [0,1], [-1,0], [0,-1], [1,1], [1,-1], [-1,1], [-1,-1]]
        
        while curr:
            nxt = []
            for node in curr:
                i, j = node
                if i == n - 1 and j == n - 1:
                    return ans
                for d in direct:
                    ii, jj = i + d[0], j + d[1]
                    if 0 <= ii < n and 0 <= jj < n and grid[ii][jj] == 0:
                        nxt.append( [ii,jj] )
                        grid[ii][jj] = 1
            curr = nxt
            ans += 1
        
        return -1
        