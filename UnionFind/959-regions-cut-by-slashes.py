# -*- coding: utf-8 -*-

'''
https://leetcode.com/problems/regions-cut-by-slashes/

Refer: https://blog.csdn.net/fuxuemingzhu/article/details/85039057
'''

class Solution(object):
    def find(self, connect, p):
        if p not in connect:
            connect[ p ] = p
        while p != connect[ p ]:
            p = connect[ p ]
        return p
    
    def union( self, connect, p, q ):
        root_p, root_q = self.find( connect, p ), self.find( connect, q )
        if root_p == root_q:
            return
        self.count -= 1
        connect[ root_q ] = root_p
        
    def regionsBySlashes(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        
        n = len(grid)
        
        self.count = n*n*4
        
        connect= {}
        
        for r in range(n):
            for c in range(n):
                if r > 0:
                    self.union( connect, (r, c, 0), ( r-1, c, 2) )
                if c > 0:
                    self.union( connect, (r, c, 3), ( r, c-1, 1) )
                if grid[r][c] != '/':
                    self.union( connect, (r, c, 0), ( r, c, 1) )
                    self.union( connect, (r, c, 2), ( r, c, 3) )
                if grid[r][c] != '\\':
                    self.union( connect, (r, c, 0), ( r, c, 3) )
                    self.union( connect, (r, c, 1), ( r, c, 2) )
        
        return self.count