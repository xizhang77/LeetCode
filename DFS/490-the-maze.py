# -*- coding: utf-8 -*-

'''
https://leetcode.com/problems/the-maze/
'''

class Solution(object):
    def dfs(self, maze, m, n, i, j, end, path):
        if [i, j] == end:
            return True
        if (i,j) in path:
            return False
        
        path.add( (i, j) )
        direct =[[1,0], [0,1],[-1,0],[0,-1]]
        for d in direct:
            ii, jj = i, j 
            while 0 <= ii + d[0] < m and 0 <= jj + d[1] < n and maze[ii+d[0]][jj+d[1]] == 0:
                ii += d[0]
                jj += d[1]
            if self.dfs( maze, m, n, ii, jj, end, path):
                return True
        
        return False
            
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        m, n = len(maze), len(maze[0])
        path = set()
        return self.dfs( maze, m, n, start[0], start[1], destination, path )