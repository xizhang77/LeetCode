# -*- coding: utf-8 -*-

'''
https://leetcode.com/problems/factor-combinations/
'''

# Solution 1: backtracking
from math import sqrt
class Solution1(object):
    def dfs(self, n, path ):
        if n < 2:
            return
        
        for i in range(2, int(sqrt(n))+1):
            if path and i < path[-1]:
                continue
            if n%i == 0:
                self.ans.append( path + [i, n/i] )
                self.dfs( n/i, path + [i] )
        
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        self.ans = []
        self.dfs( n, [] )
        
        return self.ans

# Solution 2 
class Solution2(object):
    def solver(self, start, n):
        if n < 2:
            return []
        ans = []
        for i in range( start, int(sqrt( n )) + 1 ):
            if n%i == 0:
                ans.append( [i, n/i] )
                res = self.solver( i, n/i )
                for val in res:
                    ans.append( [i] + val )
        return ans
    
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        return self.solver( 2, n )